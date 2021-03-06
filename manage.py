import os
import unittest
import coverage

from flask.ext.script import Manager

from project import app, db

manager = Manager(app)

@manager.command
def test():
    """Runs the unit tests without coverage"""
    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1

@manager.command
def cov():
    """Runs the unit tests with coverage"""
    cov = coverage.coverage(
        branch=True,
        include='project/*',
        omit=['*/__init__.py', '*/config/*']
    )
    cov.start()
    tests = unittest.TestLoader().discover('tests')
    cov.stop()
    cov.save()
    print('Coverage Summary:')
    cov.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'tmp/coverage')
    cov.html_report(directory=covdir)
    print('HTML version: file://%s/index.html' % covdir)
    cov.erase()

@manager.command
def create_db():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()

@manager.command
def create_data():
    pass

if __name__ == '__main__':
    manager.run()










