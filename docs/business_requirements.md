# Multi-Vendor E-Commerce Platform Requirements

## Users
| Name     |                                                                                                                                                                                What They Do                                                                                                                                                                                 |
|----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Customer | <ul><li>Register</li><li>Complete/Update their profiles</li><li>Browse the products</li><li>browse vendors</li><li>Search the products</li><li>Add products to cart</li><li>Order products</li><li>Watch their histories</li><li>Write review on products</li><li>Cancel their orders</li><li>Edit their orders</li><li>Give ranks to vendors</li><li>Do checkout</li></ul> |
| Vendor   |                                     <ul><li>Register</li><li>Complete/Update their profiles</li><li>List their products</li><li>Manage their inventory</li><li>Handle customer orders</li><li>Review customers</li><li>Set promotions or discounts</li><li>Package orders</li><li>Ship orders</li><li>Manage customer service</li></ul>                                     |
| Admin    |                                                                                           <ul><li>Monitor the platform</li><li>Report possible system malfunction</li><li>Add/Update/Disable vendors</li><li>Update/Disable others users<br>(Customers/Reporters/CRMs)</li></ul>                                                                                            |
| Reporter |                                                                                                                                                    <ul><li>Get selling reports</li><li>Give reports to vendors</li></ul>                                                                                                                                                    |
| CRM      |                                                                                                                                      <ul><li>Have limited access to reports</li><li>Respond to customers/vendors complaints</li></ul>                                                                                                                                       |            

## Core Flows
- **Customers** register -> complete their profile
- **Customers** search -> browse products
- **Customers** browse -> add to card
- **Customers** browse -> add to card -> checkout
- **Customers** profile -> view orders histories
- **Customers** view pending order -> cancel order
- **Customers** view pending order -> add new product
- **Customers** browse -> add review
- **Customers** view vendor -> add review
- **vendor** register -> complete their profile
- **vendor** login -> list their products
- **vendor** login -> update their products
- **vendor** login -> track and manage inventory levels -> charge items that are not available
- **vendor** process orders -> package -> ship 
- **vendor** login -> offer promotions 
- **vendor** login -> set discounts
- **vendor** respond customer inquiries
- **admin** monitor -> report system malfunction
- **admin** view list of vendors -> confirm 
- **admin** view list of vendors -> disable
- **admin** view list of vendors -> update
- **admin** view list of customers -> update/disable 
- **admin** list of users -> add role -> update/disable
- **reporter** login -> get selling reports -> send to manager
- **reporter** login -> get reports -> send to vendors
- **CRM** view limited reports -> sent to their manager
- **CRM** view limited reports -> report possible malfunctions
- **CRM** view customers/vendors complaints -> respond to them -> refer if needed