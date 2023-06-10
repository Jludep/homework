from task02_oop2 import Teacher, Student, HomeworkResult, DeadlineError
import pytest


lazy_student = Student('Roman', 'Petrov')
good_student = Student('Lev', 'Sokolov')

oop_hw = Teacher.create_homework('Learn OOP', 5)
docs_hw = Teacher.create_homework('Read docs', 5)


@pytest.fixture()
def reset_results_fixture():
    yield
    Teacher.reset_results()


@pytest.fixture()
def fill_the_dict_fixture():
    Teacher.check_homework(good_student.do_homework(oop_hw, 'content1'))
    Teacher.check_homework(lazy_student.do_homework(docs_hw, 'content2'))
    yield


def test_type_error():
    with pytest.raises(TypeError):
        HomeworkResult(good_student, "aaa", "Solution")


def test_deadline_error():
    with pytest.raises(DeadlineError):
        lazy_student.do_homework(Teacher.create_homework('NVM', 0), 'done, baby')


@pytest.mark.parametrize('hw_result', (good_student.do_homework(oop_hw, 'I have done this hw'),
                                       lazy_student.do_homework(docs_hw, 'done with no pleasure')))
def test_check_hw_positive(hw_result, reset_results_fixture):
    assert Teacher.check_homework(hw_result) is True


@pytest.mark.parametrize('hw_result', (good_student.do_homework(oop_hw, 'ahh'),
                                       lazy_student.do_homework(oop_hw, 'bee')))
def test_check_hw_negative(hw_result, reset_results_fixture):
    assert Teacher.check_homework(hw_result) is False


def test_hw_done_content(fill_the_dict_fixture, reset_results_fixture):
    assert len(Teacher.homework_done.values()) == 2


def test_hw_done_anti_plagiarism_property(reset_results_fixture):
    Teacher.check_homework(good_student.do_homework(oop_hw, 'I have done this hw'))
    f__ked_up_student = Student('Oleg', 'Second_Name')
    Teacher.check_homework(f__ked_up_student.do_homework(oop_hw, 'I have done this hw'))
    # trying to steal hw from good_student
    assert len(Teacher.homework_done) == 1  # doesn't work and there is still only 1 element in the dictionary


def test_rest_results_with_no_args(fill_the_dict_fixture):
    Teacher.reset_results()
    assert bool(Teacher.homework_done) is False


def test_rest_results_with_arg(fill_the_dict_fixture, reset_results_fixture):
    assert len(Teacher.homework_done) == 2
    Teacher.reset_results(docs_hw)
    assert len(Teacher.homework_done) == 1
    Teacher.reset_results(oop_hw)
    assert bool(Teacher.homework_done) is False