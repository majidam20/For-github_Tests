import argparse


class TaskHandler:
    """
    Handles the tasks.
    """

    def __init__(self):
        """
        Contructor of TaskHandler.
        """
        self.task_db = {}

    def receive_msg(self, msg):
        """
        Call when receiving a message.

        :param msg: the message
        """
        if msg['task_id'] not in self.task_db:
            task_entry = {'task_name': None, 'num_values': None, 'values': []}

            self.task_db[msg['task_id']] = task_entry
        else:
            task_entry = self.task_db[msg['task_id']]

        # Refacted part
        if 'task_name' in msg:
            task_entry['task_name'] = msg['task_name']
            task_entry['num_values'] = msg['num_values']
        else:
            task_entry['values'].append(msg['value'])


        if (task_entry['num_values'] is not None and
                len(task_entry['values']) == task_entry['num_values'] and
                task_entry['task_name'] is not None):

                # Error handling part
                try:
                    if task_entry['task_name'] == 'sum':
                        result = sum(task_entry['values'])
                    elif task_entry['task_name'] == 'mean':
                        result = sum(task_entry['values']) / len(task_entry['values'])
                    elif task_entry['task_name'] == 'max':
                        result = max(task_entry['values'])
                    elif task_entry['task_name'] == 'min':
                        result = min(task_entry['values'])
                    elif task_entry['task_name'] == 'count':
                        result = len(task_entry['values'])
                    elif task_entry['task_name'] == 'not_a_valid_task':
                        result = len(task_entry['values'])

                    self.output_result(result, msg['task_id'])

                # Error handling part
                except:
                    print(f"The task name \"{task_entry['task_name']}\" is not in our list")

    def output_result(self, result, task_id):
        """
        Prints results to console.

        :param result: the result
        :param task_id: the task_id
        """
        print("Task", task_id, ":", result)


def run(scenario):
    """
    This function run the scenarios an call the receive_msg function of the TaskHandler.
    This function should not be changed.
    """
    from random import shuffle

    with open(scenario) as h:
        lines = h.readlines()

    task_msgs = []
    for line in lines:
        line = line.strip()
        entries = line.split(' ')
        task_id = entries[0]
        task_name = entries[1]
        values = [int(e) for e in entries[2:]]

        task_msgs.append({'task_id': task_id, 'task_name': task_name, 'num_values': len(values)})

        # Refacted part
        task_msgs+=[({'task_id': task_id, 'value': val}) for val in values]

    shuffle(task_msgs)

    th = TaskHandler()

    for msg in task_msgs:
        th.receive_msg(msg)


if __name__ == '__main__':
    # You shouldn't have to tough anything here
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-s', '--scenario', type=int, default=None,
                        help='If set will run only a specific scenario. For example 0 for the first 1 for the second and so on.')
    args = parser.parse_args()

    scenearios = ['scenario1.txt', 'scenario2.txt', 'scenario3.txt']
    if args.scenario is not None:
        scenearios = scenearios[args.scenario:args.scenario + 1]

    for s in scenearios:
        print('*' * 35)
        print('Running scenario:', s)
        print('*' * 35)
        run(s)
        print()
