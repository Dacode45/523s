# back
Go back to previous module

## banner
New banner.

## **Check**
Sees if target is vulnerable to a particular exploit.
_Not many exploits support it_

## connect
Netcat clone. [tutorial](http://www.binarytides.com/netcat-tutorial-for-beginners/)

## **info**
Provides detailed info on module
- options
- targets
- other info

- vulnerability references (ie: CVE, BID, etc)
- payload restrictions the module may have

## irb
Ruby interpretor

## **jobs**
OPTIONS:

    -K        Terminate all running jobs.
    -h        Help banner.
    -i <opt>  Lists detailed information about a running job.
    -k <opt>  Terminate the specified job name.
    -l        List all running jobs.
    -v        Print more detailed info.  Use with -i and -l

## kill
kill backround jobs

## load

load a plugin

## unload
unloads a plugin

## **resource**
runs resource (batch) files

Some attacks such as Karmetasploit use resource files to run a set of commands in a karma.rc file to create an attack. Later on we will discuss how, outside of Karmetasploit, that can be very useful.

## **route**
The “route” command in Metasploit allows you to route sockets through a session or ‘comm’, providing basic pivoting capabilities. To add a route, you pass the target subnet and network mask followed by the session (comm) number.

also lists all routes.

## **search**
find a module
To search using a descriptive name, use the “name” keyword.

name
msf > search name:mysql

path
Use the “path” keyword to search within the module paths.
msf > search path:scada

type
Using the “type” lets you filter by module type such as auxiliary, post, exploit, etc.
msf > search type:post

multiple
You can also combine multiple keywords together to further narrow down the returned results.
msf > search cve:2011 author:jduck platform:linux

## sessions
The ‘sessions’ command allows you to list, interact with, and kill spawned sessions. The sessions can be shells, Meterpreter sessions, VNC, etc.

## **set**

The ‘set’ command allows you to configure Framework options and parameters for the current module you are working with.

```bash
msf auxiliary(ms09_050_smb2_negotiate_func_index) > set RHOST 172.16.194.134
RHOST => 172.16.194.134
msf auxiliary(ms09_050_smb2_negotiate_func_index) > show options

Module options (exploit/windows/smb/ms09_050_smb2_negotiate_func_index):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   RHOST  172.16.194.134   yes       The target address
   RPORT  445              yes       The target port
   WAIT   180              yes       The number of seconds to wait for the attack to complete.

Exploit target:

   Id  Name
   --  ----
   0   Windows Vista SP1/SP2 and Server 2008 (x86)
Metasploit also allows you the ability to set an encoder to use at run-time. This is particularly useful in exploit development when you aren’t quite certain as to which payload encoding methods will work with an exploit.
```

## **unset**
opposite of set

## **setg**
set global

## **show**
shows all modules

- exploits
- payloads
- options
- encoders

## **use**
Use a module
