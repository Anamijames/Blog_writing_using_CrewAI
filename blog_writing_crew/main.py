import warnings
from datetime import datetime

from blog_writing_crew.crew import BlogWritingCrew

warnings.filterwarnings("ignore", category=UserWarning, module="crewai")


def run():
    """Run the blog writing crew application."""
    crew_instance = BlogWritingCrew()
    inputs = {
        "topic": "How to Learn Programming as a Beginner",
        "current_year": str(datetime.now().year),
    }
    return crew_instance.crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()

