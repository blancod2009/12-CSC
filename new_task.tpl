%#template of the form for a new task
% rebase('base.tpl')
<p>Add a new task to the ToDo list:</p>
<!-- Form that sends a new task to the server. -->

<form action="/new" method="post">
  <p><input type="text" size="100" maxlength="100" name="task"></p>
<!-- Text box for entering the task. -->

  <p><input type="submit" name="save" value="save"></p>
  <!-- Saves the new task. -->

</form>

<p><a href="/todo">Home</a></p>