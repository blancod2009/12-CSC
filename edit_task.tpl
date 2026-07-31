% rebase('base.tpl')
<!-- Uses the base template for the page layout. -->

<div class="container todo-container">
<!-- Main container for the edit task page. -->
    <div class="header-section">
        <h2>Edit Task</h2>
        <p class="subtitle">Modify the details for task ID #{{number}} below:</p>
    </div>

    <form action="/edit/{{number}}" method="post" class="form-card">
     <!-- Form sends updated task information to server. -->

        <div class="form-group" style="margin-bottom: 20px;">
        <!-- Task description input. -->

            <label for="task" style="display: block; font-weight: 600; margin-bottom: 8px;">Task Description</label>
            <input type="text" id="task" name="task" value="{{current_data[0]}}" maxlength="100" class="form-control" style="width: 100%; padding: 10px; border: 1px solid var(--border-color); border-radius: var(--radius); font-size: 0.95rem;" required>
        </div>

        <div class="form-group" style="margin-bottom: 24px;">
        <!-- Status selection menu. -->
        
            <label for="status" style="display: block; font-weight: 600; margin-bottom: 8px;">Status</label>
            <select id="status" name="status" class="form-control" style="width: 100%; padding: 10px; border: 1px solid var(--border-color); border-radius: var(--radius); font-size: 0.95rem; background-color: #fff;">
            <!-- Sets current status as the selected option. -->

                <option value="open"
                % if current_data[1] == 1:
                selected
                % end
                >Open</option>
                <option value="closed"
                % if current_data[1] == 0:
                selected
                % end
                >Closed</option>
            </select>
        </div>

        <div class="form-actions" style="display: flex; gap: 12px; align-items: center; justify-content: space-between;">
            <div style="display: flex; gap: 12px; align-items: center;">
                <button type="submit" name="save" value="save" class="btn btn-primary">Save Changes</button>
                <a href="/todo" class="btn btn-outline">Cancel</a>
            </div>
            <a href="/delete/{{number}}" class="btn btn-outline" onclick="return confirm('Are you sure you want to delete this task?');">Delete Task</a>
            <!-- Asks for confirmation before deleting the task. -->

        </div>
    </form>
</div>