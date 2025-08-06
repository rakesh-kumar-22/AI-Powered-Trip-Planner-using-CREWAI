import streamlit as st
from crewai import Crew,Process
from agents import location_expert,planner_expert,guide_expert
from tasks import location_task,planner_task,guide_task

#streamlit app title

st.title("AI-Powered Trip Planner")

st.markdown("""
💡 **Plan your next trip with AI!**  
Enter your travel details below, and our AI-powered travel assistant will create a personalized itinerary including:
 Best places to visit 🎡   Accommodation & budget planning 💰
 Local food recommendations 🍕   Transportation & visa details 🚆
""")

#User Input
from_city=st.text_input("from_city",'India')
destination_city=st.text_input("destination_city","Destination Location"), 
date_from=st.date_input("Departure Date"),
date_to=st.date_input("Return Date")
interests = st.text_area("🎯 Your Interests (e.g., sightseeing, food, adventure)", "sightseeing and good food")

#Button to run crewai
if st.button("Generate Travel plan"):
    if not from_city or not destination_city or not date_from or not date_to:
        st.error("Please fill all the fields before generating your travel plan")
    else:
        st.write("AI is preparing your Travel Plan... Please wait")
        
        # Initialize Task
        loc_task=location_task(location_expert,from_city,destination_city,date_from,date_to)
        guid_task=guide_task(guide_expert,destination_city,interests,date_from,date_to)
        plan_task=planner_task([loc_task,guid_task],planner_expert,destination_city,interests,date_from,date_to)
        
        #Define Crew
        crew=Crew(
            agents=[guide_expert,location_expert,planner_expert],
            tasks=[loc_task,guid_task,plan_task],
            process=Process.sequential,
            verbose=True,
        )
        
        #Run Crew ai
        results=crew.kickoff()
        #display results
        st.subheader("Your AI powered travel plan")
        st.markdown(results)
        
        # Ensure result is a string
        travel_plan_text = str(results)  # ✅ Convert CrewOutput to string
        
        st.download_button(
            label="Download Travel Plan",
            data=travel_plan_text,
            file_name=f"Travel plan{destination_city}.txt",
            mime="text\plain"
        )
        