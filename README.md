# xERP

xERP is an open source ERP backend platform written in Python.
It is designed to be simple, easy to use and extensible.

## Features

- Simple and easy to use
- Extensible
- Open source
- Written in Python
- Web based
- Multi user

## Installation

1. Clone the repository
2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Run migrations.

```bash
python manage.py migrate
```

4. Create a super user.

```bash
python manage.py createsuperuser
```

5. Run the server.

```bash
python manage.py runserver
```

## Dependencies

- Python 3.10
- Django 5.0.4
- Django REST framework 3.13.1
- Django REST Knox 4.1.0

## TODO

- [x] Initial setup.
    - [x] Create project.
    - [x] Create app.
    - [x] Create core models.
    - [x] Create core serializers.
- [ ] Authentication Module.
    - [x] User Model.
    - [x] Register.
    - [x] Login.
    - [x] Logout.
    - [ ] Forgot Password - Send email to reset password.
    - [ ] Reset Password - Reset password.
    - [ ] Change Password.
- [ ] Profile Module.
- [ ] Write developer guidelines.
- [ ] Write authentication, profile unit test.
- [ ] Clean current code.
- [ ] HR Module.
    - [ ] Employees.
    - [ ] Departments.
    - [ ] Positions.
    - [ ] Request [Vacation, Leave, etc].
    - [ ] Integration with ZK Teco devices.
- [ ] Password Management System.
- [ ] Add more languages.
- [ ] POS.
    - [ ] Products.
    - [ ] Categories.
    - [ ] Orders.
    - [ ] Payments.
    - [ ] Discounts.
- [ ] Inventory.
    - [ ] Products.
    - [ ]  Categories.
    - [ ] Orders.
    - [ ] Stock.
    - [ ] Suppliers.
    - [ ] Purchase Orders.
- [ ] Sales.
    - [ ] Customers.
    - [ ] Orders.
    - [ ] Payments.
    - [ ] Discounts.
- [ ] Purchases.
    - [ ] Suppliers.
    - [ ] Orders.
    - [ ] Payments.
    - [ ] Discounts.
- [ ] Accounting.
    - [ ] Chart of Accounts.
    - [ ] Journal Entries.
    - [ ] Payments.
    - [ ] Receipts.
    - [ ] Invoices.
    - [ ] Reports.
- [ ] Reports.
    - [ ] Sales.
    - [ ] Purchases.
    - [ ] Inventory.
    - [ ] Accounting.
    - [ ] HR.
- [ ] Settings.
    - [ ] General.
    - [ ] Users.
    - [ ] Roles.
    - [ ] Permissions.
    - [ ] Languages.
    - [ ] Currencies.
    - [ ] Timezones.
    - [ ] Date formats.
    - [ ] Number formats.
    - [ ] Company.
    - [ ] Email.
    - [ ] SMS.
    - [ ] Notifications.
    - [ ] Backup.
    - [ ] Restore.
    - [ ] Update.
    - [ ] About.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
