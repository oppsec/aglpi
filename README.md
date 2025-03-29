<div align="center">
<img src="src/ui/aglpi.jpg" width=900>

<br>

___

<br>

<img src="https://img.shields.io/github/license/oppsec/aglpi?color=green&logo=github&style=for-the-badge">
<img src="https://img.shields.io/github/issues/oppsec/aglpi?color=green&logo=github&style=for-the-badge">
<img src="https://img.shields.io/github/stars/oppsec/aglpi?color=green&logo=github&style=for-the-badge">
<img src="https://img.shields.io/github/forks/oppsec/aglpi?color=green&logo=github&style=for-the-badge">
<img src="https://img.shields.io/github/languages/code-size/oppsec/aglpi?color=green&logo=github&style=for-the-badge">

</div>

<br>

<h3> aGLPI - against GLPI </h2>
<p> <b>aGLPI</b> is a Python script that exploits the Telemetry function added in GLPI version 9.3 and above to extract internal information from the target. </p>
<br>

<h3> What information is extracted? </h3>
<ul>
    <li>GLPI Version</li>
    <li>GLPI UUID</li>
    <li>All installed plugins and their versions</li>
    <li>GLPI usage metrics</li>
    <li>If LDAP is enabled</li>
    <li>If MailCollector is enabled</li>
    <li>Notifications system</li>
    <li>Database engine, version, size and SQL mode</li>
    <li>Web Server engine and version</li>
    <li>PHP version and all loaded modules</li>
    <li>GLPI setup settings</li>
    <li>OS type and version</li>
</ul>

<br>

<h3> Installation </h3>
<pre>
~$ apt install pipx
~$ pipx ensurepath
~$ pipx install git+https://github.com/oppsec/aglpi.git
~$ aglpi -h
</pre>

- Arch Linux based Distros: If you encounter any error when trying to install you might use <b>--break-system-packages</b> flag

<br>

<h3> Updating </h4>
<pre>
~$ pipx install git+https://github.com/oppsec/aglpi.git --force
<br>
or
<br>
~$ pipx reinstall aglpi --python /usr/bin/python
</pre>

<br>

<h3> Preview usage </h3>
<img src="https://i.imgur.com/VVEUDxv.png">
<br>

<h3> Warning </h3>
<p> The developer is not responsible for any malicious use of this tool </p>