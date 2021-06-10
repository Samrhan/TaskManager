from TaskManager import TaskManager


def test_add_a_task():
    task_manager = TaskManager()
    task_manager.add_task('Python')
    assert task_manager.task_list[0].status == 0 and task_manager.task_list[0].description == 'Python'



def test_task_good_display():
    task_manager = TaskManager()
    task_manager.add_task('Python')
    assert str(task_manager.task_list[0]) == "0 [ ] Python"


def test_generate_good_id():
    task_manager = TaskManager()
    for i in range(2):
        task_manager.add_task(i)
    for i, task in enumerate(task_manager.task_list):
        assert task.id == i


def test_remove_task():
    task_manager = TaskManager()
    for i in range(2):
        task_manager.add_task(i)
    list_len = len(task_manager.task_list)
    task_manager.remove_task(0)
    assert len(task_manager.task_list) == list_len - 1


def test_change_task_status_to_done():
    task_manager = TaskManager()
    for i in range(2):
        task_manager.add_task(i)
    for i in range(2):
        task_manager.change_status(i)
    for i in range(2):
        assert task_manager.task_list[i].status == 1


def test_change_task_status_to_todo():
    task_manager = TaskManager()
    for i in range(2):
        task_manager.add_task(i)
    for i in range(2):
        task_manager.change_status(i)
    for i in range(2):
        task_manager.change_status(i)
    for i in range(2):
        assert task_manager.task_list[i].status == 0


def test_good_task_done_display():
    task_manager = TaskManager()
    task_manager.add_task('Python')
    task_manager.change_status(0)
    assert str(task_manager.task_list[0]) == "0 [x] Python"
