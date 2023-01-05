Flask authentication app with account creation using SQLAlchemy

When run with use of "flask run" command, home page will be displayed. Login or Register page can be choosen
![image](https://user-images.githubusercontent.com/56046688/210854199-0f1371e5-bcb3-49d4-9900-07c1dbe7e484.png)

After clicking Register Page you will be redirected to this page
![image](https://user-images.githubusercontent.com/56046688/210854528-71bfc312-96cf-412b-ae30-820b8d49b97c.png)

You can then create new account that will be saved into database.

There is basic exception handling implemented:
- user with provided username exists
- password is shorter than 7 characters
- passwords does not match 

After problem is detected. Information about what went wrong will be displayed
![image](https://user-images.githubusercontent.com/56046688/210855382-b0a5efb3-1398-4a7c-90cb-95fb365309e9.png)

After successfully creating account you will be automatically redirected to login page
![image](https://user-images.githubusercontent.com/56046688/210856049-1df2e570-2ad2-4e10-8b8f-fb9d25e4284b.png)

When logged in with use of username and password provided during registration process, below page will be shown
![image](https://user-images.githubusercontent.com/56046688/210856515-e5fd1bd9-db13-4e46-a51a-0f526becd3fc.png)

If you created notes earlier they will be loaded from database. Otherwise empty box for notes will be shown.
