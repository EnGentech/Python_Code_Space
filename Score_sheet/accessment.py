import requests
from students_name import repo
from tasks import exp_repos, task_dict

marks = {
    'repo_exist': 0,
    'dir_exist': 0,
    'readme_file': 0,
    'file_exist': 0,
    'correct_output': 0,
}

score = 0
total_score = []

for st_keys, st_repo in repo.items():
    header = ("The repo belongs to {}".format(st_keys))
    print(header)
    for x in range(len(header)):
        print("=", end='')
    print('')
    url_repo = f'https://api.github.com/users/{st_repo}/repos'
    get_repo = requests.get(url_repo).json()

    # Check if the expected repo is in the students repository
    for validate in get_repo:
        rep_name = validate['name']
        if rep_name == exp_repos[1]:
            check_dir = 'pyFunctions'
            marks['repo_exist'] = 5

            # if repo exist, confirm if the expected directory has been created
            url_dir = f'https://api.github.com/repos/{st_repo}/{rep_name}/contents/{check_dir}'
            get_dir = requests.get(url_dir)
            if get_dir.status_code == 200:
                marks['dir_exist'] = 5

                # Confirm if the directory has a readme file and its not empty
                url_readme = f'https://raw.githubusercontent.com/{st_repo}/{rep_name}/main/{check_dir}/README.md'
                get_readme = requests.get(url_readme).text
                if get_readme:
                    marks['readme_file'] = 10

                    # Loop through each file and check their output
                    for index in range(len(task_dict[check_dir])):
                        url_output = f'https://raw.githubusercontent.com/{st_repo}/' \
                                     f'{rep_name}/main/{check_dir}/{task_dict[check_dir][index]}'
                        get_url_output = requests.get(url_output).text
                        if get_url_output:
                            print(get_url_output)
                            marks['file_exist'] = 10

                            # Check the output of each file
                            print('\n===== Output =====')
                            try:
                                exec(get_url_output)
                                marks['correct_output'] = int(input("Score_70%=>$ "))
                            except Exception as err:
                                print("Error: {}".format(err))
                        for value in marks.values():
                            score += int(value)
                        total_score.append(score)
                        score = 0

                        print("")
                        sum_total = 0

    result = 0
    for x in total_score:
        result += x
    if len(total_score) == 0:
        print('Final score => {}%\n'.format(result))
    else:
        denominator = len(total_score)
        result = result/denominator
        print('Final score => {}%\n'.format(result))
