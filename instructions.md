### Introduction


We would like to visually explore some (ocean) data. This data took years to collect and 
months to bring together in one location; and hopefully less than an hour to open in your
browser. The prerequisite to this procedural is having a Cloudbank log-on and a bash shell
available on your computer.


The plan is to log on to the AWS console, start a Virtual Machine (called an EC2 *instance*)
and on that machine start a Jupyter Lab server. Next we create something called an ssh tunnel
that allows us to associate a local address with that Jupyter Lab server. And then finally 
we connect so that the cloud instance is our backing engine for exploring the data that has 
been pre-installed there. The procedure is presented in 25 steps with some additional comments.
Once you navigate these steps you will have your own full-blown 
data science research environment. Don't forget to turn the lights out when you are done!


### Procedure


1. Log on to the AWS console using your credentials


2. Set your Region (upper right drop-down) to Oregon and choose Services (upper left) to see an 
array of what you can do on the AWS cloud


3. choose EC2 in the upper left region of the Services listing 


4. choose AMIs from the left sidebar


5. Ensure that the upper drop-down menu reads 'Owned By Me'
 

You should now see an AMI called `jupyter1`. 


6. select this AMI by clicking on it so a blue dot appears at left


7. choose Actions > Launch 


8. choose a VM type `c5.large` (you may have to scroll down a bit to find this)


9. choose Review and Launch at the bottom right


10. choose Launch at the bottom right


11. In the keypair dialog choose Create new keypair and name it <yourname>.pem. 
This will be the key to finding your instance in what follows.


12. Download the keypair file that is generated; then click Launch Instance in the dialog box

 
You now have a Virtual Machine ("EC2 instance") starting up on the public cloud. If you are in
a class with many people doing the same thing at the same time it can be difficult to identify
which machine is *yours*. Once you identify your computer you should name it using your name; 
just as you did for the keypair name in steps 11 and 12.

 

13. Continuing in the AWS console: Click View Instances at the lower right. This takes 
you to a table of EC2 instances (Virtual Machines), where one instance is listed per row. 
Therefore one of the rows in this table is your instance.


14. locate your instance by the key name: Scroll across to the right in the instance table to find the key name column; 
and scan down until you find your keypair name. That row will be the row for your EC2 instance.


15. Hover in the left-most box of this row--the row for your instance--to bring up a little pencil in the "Name" column


16. Click the pencil so you can enter the name of this instance. Call it <yourname>.


17. Wait for the instance state to change to running (a green dot in the Status column). 


18. While you wait for your instance to finish starting up: Write down its ip address. 
Find this address by scrolling a bit over to the right. Let's suppose for example that 
your ip address is 12.23.34.45.

 

Now you can log in to this virtual machine. Once you log in you will start a Jupyter Lab session. This session start
will give you a token -- a long string of letters and numbers -- that you will use to authenticate when you log in.

 

19.Open a bash shell and ensure the keypair file <yourname>.pem is present in your working directory.


20. Issue this command in bash: `chmod 400 yourname.pem`

 

For **Windows** Users: If you are using Windows you may need to copy the `yourname.pem` file from **Downloads** to your 
home **bash shell** directory in order to run the `chmod` command in this manner. `ssh` insists that the 
authentication key file `yourname.pem` has read-only permission; and files in your Windows User file system
can be difficult to modify (with `chmod`) in the `bash` shell. In my `bash` shell I found my Windows directory
was located at `/mnt/c/Users/myusername/`. (These are the sorts of details that can become very frustrating.)

 

21. In bash: `ssh -i yourname.pem ubuntu@12.23.34.45` to log in to your EC2 instance. (Use the correct ip address.)

 

After you respond 'yes' at the prompt you are logged on to your EC2 instance on the AWS cloud.  

 

22. On the command line of your instance: `(jupyter lab --no-browser --port=8889) &`

 

This Linux structure `(command) &` causes `command` to run in the background. You can now log out to return
to the bash prompt on your own computer. Before you do this: Notice that the above `jupyter` command produced 
several lines of output including a couple occurrences of a **token string**, as in...

 
```
...token: ae948dc6923848982349fbc48a2938d4958f23409eea427
```
 
You will need this token the first time you start up your browser session in step 25. 


23. Copy the token string and type `exit` to return to your local machine bash prompt.


24. In bash: `ssh -N -f -i yourname.pem -L localhost:7005:localhost:8889 ubuntu@12.23.34.45` with appropriate substitutions.

 

Remember that you must substitute the correct name of your .pem keypair file; and you must use the proper ip address, not 12.23.34.45. 
This command is commonly referred to as 'creating an ssh tunnel'. You are associating a location on your own computer 
with the connection point on the EC2 instance via port numbers. Your machines port 7005 is actually a tunnel to the 
EC2 instance port 8889.

 
You are almost there. The last step in this procedure is to open a new browser tab and type 'localhost:7005' in the address bar


25. In your browser address bar: `localhost:7005`

 
This should change to `localhost:7005/lab?` and a brief pause will ensue. You should be prompted for the token,  
the long string you copied from the printout in step 23. After this login / pause you should see a Jupyter lab 
environment with a notebook listed at the left called `chlorophyll.ipynb`. Click on this notebook to open it.
In the notebook you can run cells -- blocks of Python code together with explanatory sections -- 
and explore the ocean science data provided.


