from django.shortcuts import render
from rest_framework import viewsets
from .models import User , FinancialRecord
from .api import UserSerializer,FinancialRecordSerializer
from .permission import IsAdmin , IsAnalystOrAdmin
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models.functions import TruncMonth
from rest_framework.exceptions import PermissionDenied

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated()]
    
class FinancialRecordViewSet(viewsets.ModelViewSet):
    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [IsAuthenticated()]
    
        if self.action == 'create':
            return [IsAuthenticated(), IsAnalystOrAdmin()]
        
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdmin()]

        return [IsAuthenticated()]
    def perform_update(self, serializer):
        if self.request.user.role != 'admin':
            raise PermissionDenied("Only admin can update records")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user.role != 'admin':
            raise PermissionDenied("Only admin can delete records")
        instance.delete()

    def get_queryset(self):
        queryset = FinancialRecord.objects.filter(user=self.request.user)
        type = self.request.query_params.get('type')
        category = self.request.query_params.get('category')
        date = self.request.query_params.get('date')
        if type:
            queryset = queryset.filter(type=type)
        if category:
            queryset = queryset.filter(category=category)
        if date:
            queryset = queryset.filter(date=date)
 
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def summary(self, request):
        records = self.get_queryset()

        total_income = records.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        total_expense = records.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

        net_balance = total_income - total_expense

        return Response({
            "total_income": total_income,
            "total_expense": total_expense,
            "net_balance": net_balance
        })
    
    @action(detail=False, methods=['get'])
    def category_summary(self, request):
        records = self.get_queryset()

        data = records.values('category').annotate(total=Sum('amount'))

        return Response(data)
    
    @action(detail=False, methods=['get'])
    def recent(self, request):
        records = self.get_queryset().order_by('-date')[:5]

        serializer = self.get_serializer(records, many=True)
        return Response(serializer.data)
    

    @action(detail=False, methods=['get'])
    def monthly(self, request):
        records = self.get_queryset()

        data = (
            records
            .annotate(month=TruncMonth('date'))
            .values('month')
            .annotate(total=Sum('amount'))
            .order_by('month')
        )

        return Response(data)
    
