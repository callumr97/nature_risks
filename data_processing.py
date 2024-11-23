import os
import pandas as pd

dataframes = {}

for file in os.listdir("data/raw"):
    if file.endswith(".csv"):
        name = file[:-4]
        df = pd.read_csv(f"data/raw/{file}", header=2)

        df.columns = df.columns.str.replace(' ','_')

        if '#' in df.columns:
            df = df.drop(columns='#')

        df = df.loc[:, ~df.columns.str.contains('^Unnamed')] 

        dataframes[name] = df


# Merge dependency data
dependencies = pd.merge(
    dataframes['dependency_links'],
    dataframes['dependency_ratings'],
    on=['ISIC_Unique_code','ISIC_Section','ISIC_Division','ISIC_Group','ISIC_Class','ISIC_level_used_for_analysis_'],
    suffixes = ('_links','_ratings')
)

# Merge pressure data
pressures = pd.merge(
    dataframes['pressure_links'],
    dataframes['pressure_ratings'],
    on=['ISIC_Unique_code','ISIC_Section','ISIC_Division','ISIC_Group','ISIC_Class','ISIC_level_used_for_analysis'],
    suffixes=('_links','_ratings')
)

# Get the unique groups and classes for both dataframes
dependency_groups = dependencies['ISIC_Group'].unique()
dependency_classes = dependencies['ISIC_Class'].unique()

pressure_groups = pressures['ISIC_Group'].unique()
pressure_classes = pressures['ISIC_Class'].unique()

# Find differences in Groups
group_diff_in_dependencies = set(dependency_groups) - set(pressure_groups)
group_diff_in_pressures = set(pressure_groups) - set(dependency_groups)

# Find differences in Classes
class_diff_in_dependencies = set(dependency_classes) - set(pressure_classes)
class_diff_in_pressures = set(pressure_classes) - set(dependency_classes)

# Remove the rows in dependencies with unmatched Groups and Classes
dependencies_filtered = dependencies[~dependencies['ISIC_Group'].isin(group_diff_in_dependencies)]
dependencies_filtered = dependencies_filtered[~dependencies_filtered['ISIC_Class'].isin(class_diff_in_dependencies)]

# Save the cleaned dependencies and pressures
dependencies_filtered.to_csv("data/processed/dependencies.csv", index=False)
pressures.to_csv("data/processed/pressures.csv", index=False)


