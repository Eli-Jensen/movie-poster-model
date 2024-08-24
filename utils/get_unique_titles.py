import json
import os
import frozendict

# relative path
file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'popular_tmdb_endpoint_until_page_501.json')

with open(file_path, 'r') as file:
    data = json.load(file)

# Remove duplicates using JSON serialization
unique_json_list = [json.loads(t) for t in {json.dumps(d, sort_keys=True) for d in data}]

output_file_path = os.path.join(os.path.dirname(__file__), '..', 'data/popular_tmdb_endpoint_until_page_501_deduped.json')

with open(output_file_path, 'w') as outfile:
    json.dump(unique_json_list, outfile, indent=4)

print(len(unique_json_list))
print(f"File saved to {output_file_path}")


# Get just the titles
only_titles = [item['title'] for item in data]
only_titles = list(set(only_titles))
print(len(only_titles))

output_file_path = os.path.join(os.path.dirname(__file__), '..', 'data/popular_tmdb_endpoint_until_page_501_deduped_only_titles.json')

with open(output_file_path, 'w') as outfile:
    json.dump(only_titles, outfile, indent=4)

print(f"File saved to {output_file_path}")

# Get just the titles and year
only_titles_and_year = []
for item in data:
    only_titles_and_year.append(item['title']+ " - " + item['release_date'][0:4])
only_titles_and_year = sorted(list(set(only_titles_and_year)))
print(len(only_titles_and_year))

output_file_path = os.path.join(os.path.dirname(__file__), '..', 'data/popular_tmdb_endpoint_until_page_501_deduped_only_titles_and_year.json')

with open(output_file_path, 'w') as outfile:
    json.dump(only_titles_and_year, outfile, indent=4)

print(f"File saved to {output_file_path}")

# Get mapping {"Title - year" : "TMDB ID"}
all_mappings = []
seen = set()
for item in data:
    mapping = {}
    mapping['label'] = item['title']+ " - " + item['release_date']
    mapping['id']= item['id']
    if tuple(mapping.items()) in seen:
        continue
    else:
        all_mappings.append(mapping)
        seen.add(tuple(mapping.items()))
print(len(all_mappings))

output_file_path = os.path.join(os.path.dirname(__file__), '..', 'data/popular_tmdb_endpoint_until_page_501_deduped_only_titles_and_date_to_TMDB_ID.json')

with open(output_file_path, 'w') as outfile:
    json.dump(all_mappings, outfile, indent=4)

print(f"File saved to {output_file_path}")

