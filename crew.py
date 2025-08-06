from crewai import Crew,Process
from agents import location_expert,planner_expert,guide_expert
from tasks import location_task,planner_task,guide_task
crew=Crew(
    agents=[location_expert,guide_expert,planner_expert],
    tasks=[location_task,guide_task,planner_task],
    process=Process.sequential,
    share_crew=False,
    verbose=True
)

result=crew.kickoff()
print(result)