# Multi-Vendor E-Commerce Platform Data Models
# (High Level)

## User
username: str
password: str
phone: str
email: str
is_deleted: bool
status: enum 
type: enum (Customer, Vendor, CRM, Admin)
role: str(FK)

## Role
name: str

## Category
name: str
is_deleted: bool
parent_id: int (FK)

## Product
name: str
description: str
price: int
vendor: int (FK)
category: int (FK)

## ShoppingCartItem
user: int (FK)
shopping_cart: int(FK)
product: int(FK)
quantity: int
price: int

## ShoppingCart
user: int(FK)
items: ShoppingCartItem
status: enum

## Order
user: int(FK)
orders: OrderItem
total: int
status: enum

## OrderItem
user: int(FK)
product: int(FK)
order: int(FK)
quantity: int
amount: int

## Inventory
product: int(FK)
quantity: int
status: enum

## Payment
order: int(FK)
amount: int
status: enum
gateway: int

## Review
product: int(FK)
user: int(FK)
content: text
is_confirmed: bool

## Complaint
product: int(FK)
user: int(FK)
content: text
status: bool
crm_user: int(FK)

## Discount
product: int(FK)
percent: int(FK)
start_time: datetime
end_time: datetime
vendor: int(FK)
