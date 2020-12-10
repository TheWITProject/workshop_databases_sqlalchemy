# import your models

def seed(session):
    persons = [
        Person(name="Laura Jean"),
        Person(name="Bilbo Baggins"),
        Person(name="Frodo"),
    ]

    projects = [
        Project(name="Term Paper"),
        Project(name="Destroy the ring"),
    ]

    tasks = [
        Task(
            name="Write term paper",
            description="Just do it",
            due_date=datetime.date(2021,10,10),
            person_id=1,
            project_id=1,
        ),
    ]

    session.add_all(persons)
    session.add_all(projects)
    session.add_all(tasks)

    session.commit()

    session.commit()
