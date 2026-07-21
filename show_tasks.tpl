% rebase('base.tpl')
%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>The open items are as follows:</p>

<table border="1">
<tr>
    <th>ID</th>
    <th>Task</th>
    <th>Status</th>
    <th>TEST</th>
<tr>


%for row in rows:
  <tr>
    <td>{{row[0]}}</td>
    <td>{{row[1]}}</td>

<td>
    % if int(row[2]) == 1:
      open
    % else:
      closed
    % end
  </td>

  <td>
  <p><a href="/edit/6">edit</a></p>
  </td>
  
  %end
  </tr>
%end
</table>

<p><a href="/new">Add a new task</a></p>
