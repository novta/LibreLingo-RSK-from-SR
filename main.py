from librelingo_yaml_loader import yaml_loader
from librelingo_json_export.export import export_course

course = yaml_loader.load_course("./course") 
export_course("../../apps/web/src/courses/rusyn-from-serbian", course)