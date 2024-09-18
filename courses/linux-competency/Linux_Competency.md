# Basic Linux Competency with Focus on RPM
**Target Audience**: Beginners aiming to gain a strong understanding of Linux with an emphasis on RPM-based distributions.  
**Objective**: By the end of this course, learners will be able to navigate, manage, and maintain a Linux system with RPM-based package management.

---

## Section 1: Introduction to Linux and the Command Line Interface (CLI)
### Exercise: File Navigation Challenge
**Objective**: Navigate the Linux filesystem, list specific files, and create a new file.

1. **Open Terminal**:
   - Access a linux command line. I'm using `podman` to stand up a container for this course, but you can use some other cli like `docker` if you prefer.
   ```
   podman run -it centos bash
   ```
   or
   ```
   docker run -it centos bash
   ```

2. **Move to the `/usr/bin` directory**:
   - Use the `cd` command:
     ```bash
     cd /usr/bin
     ```

3. **List all files starting with the letter "s"**:
   - Use the `ls` command with a wildcard:
     ```bash
     ls s*
     ```

4. **Return to your home directory**:
   - Navigate back to the home directory using:
     ```bash
     cd ~
     ```

5. **Create a new empty file called `example.txt`**:
   - Use the `touch` command:
     ```bash
     touch example.txt
     ```

6. **Verify that the file was created**:
   - List the files in your home directory:
     ```bash
     ls
     ```

---

## Section 2: Working with Files, Permissions, and Processes
### Exercise: Permission and Ownership Task
**Objective**: Change file permissions and ownership, and understand the effect.

1. **Create a file called `myfile.txt` in your home directory**:
   - Use the `touch` command:
     ```bash
     touch ~/myfile.txt
     ```

2. **Check the default permissions**:
   - Use `ls -l` to list the file permissions:
     ```bash
     ls -l ~/myfile.txt
     ```

3. **Change file permissions so that only the owner has full access**:
   - Use the `chmod` command to set permissions to 700:
     ```bash
     chmod 700 ~/myfile.txt
     ```

4. **Verify the new permissions**:
   - Use `ls -l` to verify that the permissions have been updated:
     ```bash
     ls -l ~/myfile.txt
     ```

5. **Change the ownership of the file to another user** (replace `username` with an actual user on your system):
   - Use the `chown` command:
     ```bash
     chown username ~/myfile.txt
     ```

6. **Verify the ownership change**:
   - Use `ls -l` to confirm that the owner has changed:
     ```bash
     ls -l ~/myfile.txt
     ```

---

## Section 3: Introduction to RPM Package Management
### Exercise: Basic RPM Package Installation
**Objective**: Install, query, and verify an RPM package.

1. **Download an RPM package**:
   - Download a package from a trusted source, for example, `wget`:
     ```bash
     dnf install wget
     ```

2. **Install the RPM package**:
   - Use the `rpm -ivh` command to install the package (replace `package.rpm` with the actual filename):
     ```bash
     rpm -ivh package.rpm
     ```

3. **Verify that the package is installed**:
   - Use `rpm -q` to query the package name:
     ```bash
     rpm -q packagename
     ```

4. **Get detailed information about the package**:
   - Use `rpm -qi` to retrieve detailed package information:
     ```bash
     rpm -qi packagename
     ```

5. **Check the installation location**:
   - Use `rpm -ql` to list the files installed by the package:
     ```bash
     rpm -ql packagename
     ```

---

## Section 4: Advanced RPM Usage
### Exercise: Upgrading and Rolling Back RPM Packages
**Objective**: Upgrade a package and roll back to a previous version.

1. **Install an older version of a package**:
   - Download and install an older version of a package:
     ```bash
     rpm -ivh oldversion.rpm
     ```

2. **Verify the installed version**:
   - Use `rpm -qi` to check the package version:
     ```bash
     rpm -qi packagename
     ```

3. **Upgrade the package to the latest version**:
   - Download the latest version and install it with `rpm -Uvh`:
     ```bash
     rpm -Uvh latestversion.rpm
     ```

4. **Verify the new version**:
   - Check the updated version:
     ```bash
     rpm -qi packagename
     ```

5. **Rollback to the previous version**:
   - Use the `rpm --rollback` command:
     ```bash
     rpm --rollback
     ```

6. **Verify that the rollback was successful**:
   - Query the package version again to ensure it reverted:
     ```bash
     rpm -qi packagename
     ```

---

## Section 5: Mastering YUM/DNF for Package Management
### Exercise: Repository Configuration and Software Group Installation
**Objective**: Add a repository and install a software group.

1. **Add the EPEL repository**:
   - Install the EPEL repository for additional packages:
     ```bash
     dnf install epel-release
     ```

2. **Verify the repository has been added**:
   - List all configured repositories:
     ```bash
     dnf repolist
     ```

3. **Install the "Development Tools" group**:
   - Use `dnf` to install a group of development tools:
     ```bash
     dnf groupinstall "Development Tools"
     ```

4. **Verify the installation**:
   - Check that the group was installed by listing installed groups:
     ```bash
     dnf grouplist installed
     ```

---

## Section 6: Basic System Administration
### Exercise: Service and User Management
**Objective**: Create a user, assign them to a group, and manage a service.

1. **Create a new user named `adminuser`**:
   - Use the `useradd` command to create the user:
     ```bash
     useradd adminuser
     ```

2. **Assign the user to the `wheel` group**:
   - Use the `usermod` command to add the user to the group:
     ```bash
     usermod -aG wheel adminuser
     ```

3. **Set a password for the user**:
   - Use the `passwd` command:
     ```bash
     passwd adminuser
     ```

4. **Enable the `httpd` service to start on boot**:
   - Use `systemctl` to enable the service:
     ```bash
     systemctl enable httpd
     ```

5. **Start the `httpd` service**:
   - Start the service immediately:
     ```bash
     systemctl start httpd
     ```

6. **Verify the service is running**:
   - Check the service status:
     ```bash
     systemctl status httpd
     ```

---

## Section 7: Networking Basics
### Exercise: Basic Network Troubleshooting
**Objective**: Test network connectivity and troubleshoot with basic tools.

1. **Check network connectivity using `ping`**:
   - Ping Google’s server:
     ```bash
     ping google.com
     ```

2. **Trace the network route using `traceroute`**:
   - Use the `traceroute` command to see the path to a domain:
     ```bash
     traceroute google.com
     ```

3. **Display your machine’s network interfaces**:
   - Use `ifconfig` or `ip a`:
     ```bash
     ifconfig
     # OR
     ip a
     ```

---

## Section 8: Scripting and Automation
### Exercise: Automating a Backup Script
**Objective**: Write a shell script to back up files and schedule it with `cron`.

1. **Create the backup script**:
   - Write the following script to back up the `/home/user/Documents` directory:
     ```bash
     nano backup.sh
     ```

   Inside the file:
     ```bash
     #!/bin/bash
     tar -czvf /home/user/backup.tar.gz /home/user/Documents
     ```

2. **Make the script executable**:
   - Use `chmod` to give execution permission:
     ```bash
     chmod +x backup.sh
     ```

3. **Schedule the script to run daily at midnight**:
   - Open the cron table:
     ```bash
     crontab -e
     ```

   Add the following line to schedule the script:
     ```bash
     0 0 * * * /home/user/backup.sh
     ```

4. **Verify the cron job**:
   - Check the scheduled jobs:
     ```bash
     crontab -l
     ```

---

## Section 9: Basic Security and Hardening
### Exercise: SELinux and Firewall Configuration
**Objective**: Understand SELinux and configure the firewall.

1. **Check the current status of SELinux**:
   - Use `getenforce` to check if SELinux is enforcing:
     ```bash
     getenforce
     ```

2. **Enable SELinux if it’s disabled**:
   - Edit `/etc/selinux/config` and set it to enforcing:
     ```bash
     nano /etc/selinux/config
     ```

   Change `SELINUX=disabled` to `SELINUX=enforcing`.

3. **Check firewall rules**:
   - Use `firewall-cmd` to list the active zones and rules:
     ```bash
     firewall-cmd --list-all
     ```

4. **Add a rule to allow HTTP traffic**:
   - Use `firewall-cmd` to allow HTTP service:
     ```bash
     firewall-cmd --permanent --add-service=http
     firewall-cmd --reload
     ```

5. **Verify the new rule**:
   - List the rules again to check if HTTP has been allowed:
     ```bash
     firewall-cmd --list-all
     ```

---

## Section 10: Disk Management and Partitioning
### Exercise: Manage Partitions with `fdisk`
**Objective**: Create and format a new partition.

1. **List all disk devices**:
   - Use the `fdisk` command to list all disks:
     ```bash
     fdisk -l
     ```

2. **Select the disk to partition** (replace `/dev/sdb` with your actual disk):
   - Use `fdisk` to interact with the disk:
     ```bash
     fdisk /dev/sdb
     ```

3. **Create a new partition**:
   - Follow the on-screen instructions to create a primary partition.

4. **Format the partition**:
   - Use `mkfs` to format the partition as ext4:
     ```bash
     mkfs.ext4 /dev/sdb1
     ```

5. **Mount the partition**:
   - Create a mount point and mount the new partition:
     ```bash
     mkdir /mnt/newpartition
     mount /dev/sdb1 /mnt/newpartition
     ```

6. **Verify the partition is mounted**:
   - Use `df -h` to check the mounted partitions:
     ```bash
     df -h
     ```

---

## Section 11: Backup and Restore Strategies
### Exercise: Creating Incremental Backups with `rsync`
**Objective**: Perform incremental backups using `rsync`.

1. **Create a directory for backup**:
   - Create a directory named `backup`:
     ```bash
     mkdir ~/backup
     ```

2. **Run an `rsync` backup**:
   - Backup the `/home/user/Documents` directory to the `backup` directory:
     ```bash
     rsync -av --progress /home/user/Documents ~/backup
     ```

3. **Modify a file in the source directory**:
   - Make changes to a file in `/home/user/Documents`.

4. **Run an incremental backup**:
   - Use `rsync` again to perform an incremental backup:
     ```bash
     rsync -av --progress /home/user/Documents ~/backup
     ```

5. **Verify that only the modified files were backed up**:
   - Check the output to ensure that only changed files were transferred.

---

## Section 12: Course Review and Capstone Project
### Capstone Project: Setting Up a Python Web Application with the LEMP Stack
**Objective**: Set up and configure a Python-based web application on a LEMP stack (Linux, Nginx, MySQL, Python with Flask).

1. **Install Nginx**:
   - Install the Nginx web server using `dnf`:
     ```bash
     dnf install nginx
     ```

2. **Start and enable Nginx**:
   - Start Nginx and ensure it runs on boot:
     ```bash
     systemctl start nginx
     systemctl enable nginx
     ```

3. **Install MySQL/MariaDB**:
   - Install MariaDB (or MySQL) for your database layer:
     ```bash
     dnf install mariadb-server mariadb
     ```

4. **Start and enable MariaDB**:
   - Start the database service and enable it at boot:
     ```bash
     systemctl start mariadb
     systemctl enable mariadb
     ```

5. **Secure the MariaDB installation**:
   - Secure the MariaDB installation by setting a root password and removing test databases:
     ```bash
     mysql_secure_installation
     ```

6. **Create a database for your Flask application**:
   - Log into MariaDB and create a new database:
     ```bash
     mysql -u root -p
     CREATE DATABASE flaskapp;
     CREATE USER 'flaskuser'@'localhost' IDENTIFIED BY 'password';
     GRANT ALL PRIVILEGES ON flaskapp.* TO 'flaskuser'@'localhost';
     FLUSH PRIVILEGES;
     ```

7. **Install Python and Flask**:
   - Install Python 3 and `pip` (Python's package manager):
     ```bash
     dnf install python3 python3-pip
     ```

   - Install Flask and any other necessary Python packages:
     ```bash
     pip3 install flask pymysql
     ```

8. **Create a Flask application**:
   - Create a new directory for your Flask app:
     ```bash
     mkdir ~/flaskapp
     cd ~/flaskapp
     ```

   - Create a simple Flask application (`app.py`):
     ```python
     from flask import Flask
     app = Flask(__name__)

     @app.route('/')
     def hello():
         return "Hello, Flask with Nginx and MySQL!"

     if __name__ == "__main__":
         app.run(host='0.0.0.0')
     ```

9. **Test the Flask app**:
   - Run the Flask app locally to ensure it's working:
     ```bash
     python3 app.py
     ```

   - Visit `http://localhost:5000` in your browser to see the "Hello, Flask with Nginx and MySQL!" message.

10. **Configure Nginx to Serve the Flask App**:
    - Create an Nginx configuration file for your Flask app:
      ```bash
      nano /etc/nginx/conf.d/flaskapp.conf
      ```

    - Add the following configuration to proxy pass requests to the Flask app:
      ```nginx
      server {
          listen 80;
          server_name localhost;

          location / {
              proxy_pass http://127.0.0.1:5000;
              proxy_set_header Host $host;
              proxy_set_header X-Real-IP $remote_addr;
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
              proxy_set_header X-Forwarded-Proto $scheme;
          }
      }
      ```

11. **Restart Nginx**:
    - After configuring Nginx, restart the service to apply the changes:
      ```bash
      systemctl restart nginx
      ```

12. **Access the Flask app via Nginx**:
    - Visit `http://localhost` in your browser. Nginx should now be serving your Flask application.

13. **Connect Flask to MySQL**:
    - Modify your `app.py` to connect to MySQL using `pymysql`:
     ```python
     from flask import Flask
     import pymysql

     app = Flask(__name__)

     connection = pymysql.connect(
         host='localhost',
         user='flaskuser',
         password='password',
         db='flaskapp'
     )

     @app.route('/')
     def hello():
         return "Connected to MySQL with Flask!"

     if __name__ == "__main__":
         app.run(host='0.0.0.0')
     ```

14. **Finalize the Project**:
    - Your Python-based web application with Nginx, MySQL, and Flask is now complete. Test all functionality and verify that the app is connecting to MySQL and serving through Nginx.

---
