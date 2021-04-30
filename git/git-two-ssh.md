

having a faster git by using ssh 
==============================================

problem
==============================================  
When you use git to manage and develop packages for some projects, you may encounter some problems, like error 110, error 443 and so on. It is best for you to change your agreement from http(s) to ssh.  
solution  
=================================================
```Shell,default
## enter you home dictionary<div><br/></div>$cd<div><br/></div><div><br/></div>## add your GitHub email and passphrase to ssh-keygen<div><br/></div>#tip:If you are too old system that does not support the Ed25519 algorithm, you need to use this commmand:<div><br/></div>#ssh-keygen -t rsa -b 4096 -C "email_address@example.com"<div><br/></div>$ssh-keygen -t ed25519 -C "email_address@example.com"<div><br/></div>Generating public/private ed25519 key pair<div><br/></div>Enter a file in which to save the key(/your_path/.ssh/id_ed25519):#just press enter to use the default path<div><br/></div>Enter passphrase:#input a passphrase like a passwd which will be used for verify your identity when used ssh for git<div><br/></div>Enter same passphrase again:#just input again<div><br/></div><div><br/></div>#Copy the ssh public key <div><br/></div>$cat /your_path/.ssh/id_ed25519.pub #Copy all words<div><br/></div>
```

Add a ssh for your GitHub  
--------------------------------------------------------------------------------------------------------------------------------
Open the setting of your GitHub, like this:
![QQ截图20210430151835.png](file:///C:/APP/%E4%B8%BA%E7%9F%A5%E7%AC%94%E8%AE%B0/%E6%95%B0%E6%8D%AE%E6%96%87%E4%BB%B6/temp/811f7b82-3cea-4ff3-beb6-75be452e7ca3/128/index_files/QQ%E6%88%AA%E5%9B%BE20210430151835.png)

![QQ截图20210430151848.png](file:///C:/APP/%E4%B8%BA%E7%9F%A5%E7%AC%94%E8%AE%B0/%E6%95%B0%E6%8D%AE%E6%96%87%E4%BB%B6/temp/811f7b82-3cea-4ff3-beb6-75be452e7ca3/128/index_files/QQ%E6%88%AA%E5%9B%BE20210430151848.png)

Then click New SSH key, like this
![QQ截图20210430151900.png](file:///C:/APP/%E4%B8%BA%E7%9F%A5%E7%AC%94%E8%AE%B0/%E6%95%B0%E6%8D%AE%E6%96%87%E4%BB%B6/temp/811f7b82-3cea-4ff3-beb6-75be452e7ca3/128/index_files/QQ%E6%88%AA%E5%9B%BE20210430151900.png)

Paste what you just copied to Key,then have a name for your key, like my thinkpad  

```Shell,default
#Finally you need to change your project's git aggreement<div><br/></div>#enter a git project<div><br/></div>$cd /{your_path}/{your_git_name}/<div><br/></div><div><br/></div>#change url<div><br/></div>$vim .git/config<div><br/></div>#you will see something, like this:<div><br/></div>url = https://github.com/{your_GitHub_name}/{your_git_name}.git<div><br/></div>        fetch = +refs/heads/*:refs/remotes/origin/*<div><br/></div>#just change  ,like this:<div><br/></div>[remote "origin"]<div><br/></div>        url = git@github.com:{your_GitHub_name}/{your_git_name}.git<div><br/></div>        fetch = +refs/heads/*:refs/remotes/origin/*
```

Now, you can use it, like this:
```Shell,default
##test<div><br/></div>$git pull<div><br/></div>Enter passphrase for key '/{your_path}/.ssh/id_ed25519':#input your passphrase<div><br/></div>
```

