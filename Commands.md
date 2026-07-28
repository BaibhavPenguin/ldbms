# LDBMS Shell Commands
<font color='yellow'><strong>help - Get an overview of supported LDBMS commands.
</strong></font><br>
<code>help</code> - Prints a basic overview of supported commands  
<code>help &lt;command&gt;</code> - Prints detailed information about a specific command.
<hr>

<font color='yellow'><strong>clear - Clear the LDBMS terminal.
</strong></font><br>
<code>clear</code> - Clears the screen.  
<hr>

<font color='yellow'><strong>cls - Clear the LDBMS terminal (Windows Legacy Terminals).
</strong></font> <br>
<code>cls</code> - Clears the screen.
<hr>

<font color='yellow'><strong>use - Change the current database.
</strong></font><br>
<code>use &lt;database_name&gt;</code> - Changes the current database to <code>database_name</code> , all following queries affect <code>database_name</code>
<hr>

<font color='yellow'><strong>database - View the path and name of the active database.
</strong></font><br>
<code>database</code> - Prints the name & path of the active database
<hr>

<font color='yellow'><strong>show - View the path and name of the active database.
</strong></font><br> 
<code>show &lt;databases&gt;</code> - Shows list of all indexed databases <br>
<code>show &lt;tables&gt;</code> - Shows the tables in a databases <br>
<code>show &lt;index&gt;</code> - Shows indexed attributes of a specified table <br>
<code>show &lt;indexes&gt;</code> - Shows all indexes<br>
<code>show &lt;views&gt;</code> - Shows all tables with type view<br>
<code>show columns from  &lt;table_name&gt;</code> - Shows all the columns from a table<br>
<code>show create database <database_name></code> - Shows the schema used to create the database <br>
<code>show create table <table_name></code> - Shows the schema used to create the table <br>
<code>show create trigger <trigger_name></code> - Shows the schema used to create the trigger <br>
<code>show create view <view_name></code> - Shows the schema used to create the view <br>

<hr>
<font color='yellow'><strong>index - Add an already existing database to LDBMS index.</strong></font> <br>
<code>index &lt;database_name&gt; &lt;database_path&gt;</code> - Indexes local database located at <code>&lt;database_path&gt;</code> under <code>&lt;database_name&gt;</code> <br>
<hr>
<font color='yellow'><strong>history - Show list of previously executed ldbms commands.</strong></font> <br>
<code>history</code> - Shows list of previously executed ldbms commands on the terminal. It shows upto 10 recent commands and automatically deletes the oldest command when more than 10 commands were executed.

<hr>
<font color='yellow'><strong>export - Save all the commands executed in the current session in a file.</strong></font> <br>
<code>export &lt;path_to_file&gt;</code> - Exports all the successful commands from the current session into a text file.

## OTHER COMMANDS WILL BE ADDED SOON.
This is an incomplete set as the app is still in development and I have no time to push regular commits espicially about commands. However the In-App Help documentation is always up to date so you can get this information from directly within LDBMS.












