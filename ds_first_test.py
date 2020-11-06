import json

JSON_FILE = 'source_file_2.json'

def get_priority(data):
    return data[1]

def run():
    json_data = open(JSON_FILE).read()
    projects_data = json.loads(json_data)

    managers_priority = {}
    watchers_priority = {}

    for project in projects_data:
        for w in project.get('watchers', []):
            if watchers_priority.get(w):
                watchers_priority[w].append((project['name'], project['priority']))
            else:
                watchers_priority[w] = [(project['name'], project['priority'])]

        for w in project.get('managers', []):
            if managers_priority.get(w):
                managers_priority[w].append((project['name'], project['priority']))
            else:
                managers_priority[w] = [(project['name'], project['priority'])]

    for manager in managers_priority:
        managers_priority[manager].sort(key=get_priority)
    for watcher in watchers_priority:
        watchers_priority[watcher].sort(key=get_priority)

    managers = {}
    watchers = {}

    for manager in managers_priority:
        managers[manager] = []
        for item in managers_priority[manager]:
            managers[manager].append(item[0])
    
    for watcher in watchers_priority:
        watchers[watcher] = []
        for item in watchers_priority[watcher]:
            watchers[watcher].append(item[0])
    managers_json = open('managers.json', 'w')
    managers_json.write(json.dumps(watchers, indent=4, sort_keys=True))
    managers_json.close()
    
    watchers_json = open('watchers.json', 'w')
    watchers_json.write(json.dumps(managers, indent=4, sort_keys=True))
    watchers_json.close()
    
if __name__ == '__main__':
    run()