#!/usr/bin/env python
# coding: utf-8

# In[2]:


from dataclasses import dataclass, field
from datetime import datetime, timezone


# In[6]:


@dataclass
class Orders:
    id: int
    OrderDate: datetime
    ExpectedDeliveryDate: datetime
    CustomerPON: str
    IsUndersupplyBO: bool
    Comments: str
    DeliveryInstructions: str
    InternalComments: str
    PickingCompletedWhen: datetime
    
    def __gt__(self, other):
        return self.OrderDate > other.OrderDate
    def __ge__(self, other):
        return self.OrderDate >= other.OrderDate


# In[7]:


@dataclass
class Invoices:
    id: int
    InvoiceDate: datetime
    CustomerPON: str
    IsCreditNote: bool
    CreditNoteReason: str
    Comments: str
    DeliveryInstructions: str
    InternalComments: str
    TotalDryItems: int
    TotalChillerItems: int
    DeliveryRun: str
    RunPosition: str
    ReturnedDeliveryData: str
    ConfirmedDeliveryTime: datetime
    ConfirmedReceivedBy: str
    
    def __gt__(self, other):
        return self.OrderDate > other.OrderDate
    def __ge__(self, other):
        return self.OrderDate >= other.OrderDate


# In[5]:


@dataclass
class Customers:
    id: int
    CustomerName: str
    CreditLimit: float
    AccountOpenedDate: datetime
    StandardDiscountP: float
    IsStatementSent: bool
    IsOnCreditHold: bool
    PaymentDays: int
    PhoneNumber: str
    FaxNumber: str
    DeliveryRun: str
    RunPosition: str
    URL: str
    DeliveryAddressLine1: str
    DeliveryAddressLine2: str
    DeliveryPostalCode: str
    DeliveryLocation: list
    PostalAddressLine1: str
    PostalAddressLine2: str
    PostalPostalCode: str
    


# In[ ]:




