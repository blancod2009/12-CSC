% rebase('base.tpl')

<div class="container todo-container">
<!-- Main container for the task list. -->

    <div class="header-section">
        <h2>Task Management</h2>
        <p class="subtitle">Here is the current list of tasks from your database:</p>
    </div>

    <div class="table-responsive">
    <!-- Displays the task table. -->

        <table class="premium-table">
            <thead>
            <!-- Table headings. -->

                <tr>
                    <th class="col-id">ID</th>
                    <th class="col-task">Task Description</th>
                    <th class="col-status">Status</th>
                    <th class="col-actions">Actions</th>
                </tr>
            </thead>
            <tbody>
                % for row in rows:
                <!-- Loops through each task in database. -->

                <tr>
                    <td class="col-id">#{{row[0]}}</td>
                    <td class="col-task">{{row[1]}}</td>
                    <td class="col-status">
                        % if int(row[2]) == 1:
                            <span class="badge badge-open">Open</span>
                        % else:
                            <span class="badge badge-closed">Closed</span>
                        % end
                    </td>
                    <td class="col-actions">
                        <a href="/edit/{{row[0]}}" class="btn btn-sm btn-outline">Edit</a>
                        <!-- Opens edit page for selected task. -->
                        
                    </td>
                </tr>
                % end
            </tbody>
        </table>
    </div>

    <div class="actions-footer">
        <a href="/new" class="btn btn-primary">+ Add a New Task</a>
        <!-- Button to create a new task. -->
        
    </div>
</div>