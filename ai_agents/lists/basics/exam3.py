search_results = ["Result H", "Result B", "Result C"]
database_results = ["Result D", "Result E"]
api_results = ["Result F", "Result G"]

all_results=search_results+database_results+api_results
print(all_results)

combined=search_results.copy()
combined.extend(database_results+api_results)
print(combined)

combined.sort()
print(combined)

def combine(*lists):
    combined=[]
    for lst in lists:
        combined.extend(lst)
    return list(set(combined))
    
list1=["Result H", "Result B", "Result C","Result F", "Result G"]
list2=["Result D", "Result E"]
list3=["Result F", "Result G"]
combined_lists=combine(list1,list2,list3)
print(combined_lists)


# Agent collects data from multiple sources
def gather_all_info(query):
    web_results = search_web(query)
    db_results = search_database(query)
    memory_results = search_memory(query)
    
    # Combine all results
    all_results = web_results + db_results + memory_results
    
    # Remove duplicates (by content)
    seen = set()
    unique_results = []
    for result in all_results:
        if result not in seen:
            seen.add(result)
            unique_results.append(result)
    
    print(f"Found {len(unique_results)} unique results across sources")
    return unique_results

def search_web(query):
    return ["Web: Paris is capital", "Web: Population 2M"]

def search_database(query):
    return ["DB: Capital of France", "DB: Official language French"]

def search_memory(query):
    return ["Memory: Visited Paris last year"]

results = gather_all_info("Paris")
for result in results:
    print(f"  {result}")