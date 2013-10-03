#TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.run_tests'
#TEST_OUTPUT_VERBOSE = True
#TEST_OUTPUT_DESCRIPTIONS = True
#TEST_OUTPUT_DIR = 'xmlrunner'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--exclude=selenium']

