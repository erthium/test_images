PY := python3
FLAGS := -b
SRC_DIR := src
CREATOR := $(SRC_DIR)/creator.py

DATA_DIR := data
LATEST_DATA_DIR := latest_data

REQUIREMENTS_FILE := requirements.txt


sure=0

.PHONY: init freeze create nuke_data

init:
	pip install -r $(REQUIREMENTS_FILE)


freeze:
	pip freeze > $(REQUIREMENTS_FILE)


create:
	@$(PY) $(FLAGS) $(CREATOR)


nuke_data:
	@([ $(sure) -eq 1 ] && rm -rf $(DATA_DIR)/*) || echo "Please set sure=1 to nuke data"
