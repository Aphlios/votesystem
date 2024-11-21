# Voting System 

**This is a repo of CISC7403 Project For group B7**

## Document structure: 	

```
votesystem/
├── docker-compose.yml
├── voting/
│   ├── Dockerfile
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
├── result/
│   ├── Dockerfile
│   ├── app.py
│   ├── templates/
│   │   └── result.html
└── database/
    ├── Dockerfile
    └── init.sql
```

## How to Begin?

First, you should make sure your computer have docker installed and opened, then running Terminal Instruction `docker-compose up --build`  at the root directory of the project.

For Example:

![example.png](images%2Fexample.png)

Also you should shut down your own postgreSQL service if you have installed it in your computer, to free the port 5432 for running our project.

You can using the link  <http://localhost:6110/> to get in the voting system, and vote for the dogs and cats.
You will see somthing like this:

![voting.png](images%2Fvoting.png)

This page has two buttons. When you press one of the buttons, you will trigger an event inside the container and simultaneously redirect to the vote success page.
**Success Page** as shown in the image below.

![success.png](images%2Fsuccess.png)

On this page, if you click 'View Results', you will be redirected to the data display page of another container. If you choose 'Continue Voting', you will return to the previous page to continue voting
**Results Display page** as shown in the image below:

![results.png](images%2Fresults.png)

You can also choose to directly visit the <http://localhost:6111/> to view the results.
Finally, in the Docker logs, you can see detailed records of button click events. Like the example below!

![log.png](images%2Flog.png)
