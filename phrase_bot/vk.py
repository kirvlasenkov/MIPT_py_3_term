import os
import vk_api
from dotenv import load_dotenv
import time


# Downloading of environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

VK_LOGIN = os.getenv('VK_LOGIN')
VK_PASSWORD = os.getenv('VK_PASSWORD')
GROUP_ID = os.getenv("mipt_prepod_public_id")


def authorize(vk_login, vk_password) -> "class 'vk_api.vk_api.VkApiMethod'":
    '''
    More convenient vk authorization process
    :param vk_login: user's vk login
    :param vk_password: user's vk password
    :return: some vk instance, which ready
    to do almost all methods of vk interface
    '''
    vk_session = vk_api.VkApi(vk_login, vk_password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error:
        print("wrong authorization data!")
        return
    else:
        vk = vk_session.get_api()
        return vk


def get_wall_post(vk, group_id, file) -> None:
    '''
    Probably returns all posts from
    public's page
    :param vk: product of \'get_api\' method
    :param vk: group id
    :param file: output file, which usef for
    collecting data from group\'s wall
    '''

    with open(file, "w") as data_file:
        for bias in range(60):
            posts = vk.wall.get(owner_id=group_id,
                                count=100,
                                filter='owner',
                                offset=100 * bias
                                )
            for post in posts["items"]:
                data_file.write(post['text'])


if __name__ == '__main__':
    start = time.time()

    vk = authorize(VK_LOGIN, VK_PASSWORD)
    # get_wall_post(vk, GROUP_ID, "phrases.txt")

    end = time.time()
    print(end - start)
