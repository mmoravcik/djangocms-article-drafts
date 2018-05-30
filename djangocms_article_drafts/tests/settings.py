from djangocms_helper import runner


HELPER_SETTINGS = {
    'INSTALLED_APPS': [
        'djangocms_article_drafts.test_project',
    ]
}


def run():
    runner.cms('djangocms_article_drafts')


if __name__ == '__main__':
    run()

