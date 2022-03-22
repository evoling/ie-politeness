library(tidyverse)
library(readxl)
library(forcats)
# data <- read_excel("~/Dropbox/Projects/ie-politeness/supplementary_materials/ie-politeness/data/SAEfeatures-current.xlsx", range=cell_cols("A:J"))
data <- read_excel("SAEfeatures-current.xlsx", range=cell_cols("A:J"))
names(data) <- c("language", "articles", "relatives", "have_perfect", 
                 "participial_passive", "dative_external_poss", "negation", 
                 "equative", "subject_agreement", "intens_refl") 
data <- data %>%
  mutate(across(everything(), function(e) fct_recode(e, "1"="yes", "0"="no"))) %>% 
  write_tsv(paste0("SAE-features-",nrow(.) ,".csv")) 
