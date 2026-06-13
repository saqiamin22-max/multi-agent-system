from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain


def run_research_pipeline(topic: str) -> dict:
    state = {}

    # Step 1 - Search Agent
    print("\n" + "*" * 50)
    print("Step 1 - Search agent is working...")
    print("=" * 50)

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })

    state['search_result'] = search_result['messages'][-1].content
    print("\nSearch Result (short):\n", state['search_result'][:300])

    # Step 2 - Reader Agent
    print("\n" + "*" * 50)
    print("Step 2 - Reader agent is scraping...")
    print("=" * 50)

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
                      f"From the search results below about '{topic}', pick ONLY a direct article URL "
                      f"(not homepage, not category page), then scrape it.\n\n"
                      f"Search Results:\n{state['search_result'][:800]}"
                      )]
    })

    state['scraped_content'] = reader_result['messages'][-1].content
    print("\nScraped Content (short):\n", state['scraped_content'][:500])

    # Step 3 - Writer
    print("\n" + "*" * 50)
    print("Step 3 - Writing report...")
    print("=" * 50)

    research_combined = (
        f"SEARCH RESULTS:\n{state['search_result']}\n\n"
        f"SCRAPED CONTENT:\n{state['scraped_content']}"
    )

    state['report'] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\nFinal Report:\n", state['report'][:500])

    # Step 4 - Critic
    print("\n" + "*" * 50)
    print("Step 4 - Critic reviewing...")
    print("=" * 50)

    state['feedback'] = critic_chain.invoke({
        "report": state['report']
    })

    print("\nCritic Feedback:\n", state['feedback'])

    return state

if __name__ == "__main__":
    try:
        topic = input("Enter a research topic: ").strip()

        if topic == "":
            print("Please enter a topic!")
        else:
            run_research_pipeline(topic)

    except KeyboardInterrupt:
        print("\nProgram stopped by user (Ctrl + C)")