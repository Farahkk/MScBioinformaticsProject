#!/usr/bin/python3
import cgi
from pymongo import MongoClient
import sys
import re
import json
#to send the python error messages to the Web browser
import cgitb
cgitb.enable()

#-------------------------------------------------------------------------------
def mongo_connect(user, password, host, path, clusterName, collectionName):
    """
    Call this with:
    collection = mongo_connect()
    """
   
    # Parameters for connecting to the database (which you can obtain from your Atlas account
    # See documentation at https://www.mongodb.com/docs/manual/reference/connection-string/
    options        = "?retryWrites=true&w=majority"

    #Connecting to the MongoDB database/collection
    url            = "mongodb+srv://" + user + ":" + password + "@" + host + path + options
    cluster        = MongoClient(url)
    db             = cluster[clusterName]
    collection     = db[collectionName]
    return collection

#-------------------------------------------------------------------------------
'''def add_to_query(query_parts, key, value, yesno):
    query = ''
    if yesno == "yes":
        query  = "{ \"$or\" : [\n"    #Initialize ORing
        query += "{\"%s\" : {\"$regex\" : \".*%s.*\"}}" % (key, value)
        for i in range(1,6):
            query += ",\n {\"%s[%d]\" : {\"$regex\" : \".*%s.*\"}}" % (key, i, value)
        query += "\n] }\n";
    elif yesno == "no":
        query  = "{ \"$and\" : [\n"    #Initialize ANDing
        query += "{\"%s\" : {\"$not\": {\"$regex\" : \".*%s.*\"}}}" % (key, value)
        for i in range(1,6):
            query += ",\n {\"%s[%d]\" : {\"$not\": {\"$regex\" : \".*%s.*\"}}}" % (key, i, value)
        query += "\n] }\n";

    if query != "":
        query_parts.append(query)
    return query_parts;'''


#An alternative version of add_to_query() which makes the searches case insensitive,
#so you don't need to worry about 'reduce' vs 'Reduce', etc.

def add_to_query(query_parts, key, value, yesno):
    query = ''
    if yesno == "yes":
        query  = "{ \"$or\" : [\n"    #Initialize ORing
        query += "{\"%s\" : {\"$regex\" : \".*%s.*\", \"$options\" : \"i\"}}" % (key, value)
        for i in range(1,6):
            query += ",\n {\"%s[%d]\" : {\"$regex\" : \".*%s.*\", \"$options\" : \"i\"}}" % (key, i, value)
        query += "\n] }\n";
    elif yesno == "no":
        query  = "{ \"$and\" : [\n"    #Initialize ANDing
        query += "{\"%s\" : {\"$not\": {\"$regex\" : \".*%s.*\", \"$options\" : \"i\"}}}" % (key, value)
        for i in range(1,6):
            query += ",\n {\"%s[%d]\" : {\"$not\": {\"$regex\" : \".*%s.*\", \"$options\" : \"i\"}}}" % (key, i, value)
        query += "\n] }\n";

    if query != "":
        query_parts.append(query)
    return query_parts;

#-------------------------------------------------------------------------------
# Combines the individual query parts into one query
def combine_query_parts(query_parts):
    query = ''

    if len(query_parts) == 0:
        # Everything is don't care so we will need the whole list back
        return('')
    elif len(query_parts) == 1:
        # Only one item so no ANDing
        return(query_parts[0])

    line_num = 0                           # Used to count through the lines
    query    = "{ \"$and\" : [\n"          # Initialize ANDing
    for line in query_parts:
        query    += "         " + line     # Add this line (spaces are just formatting for debugging!)
        line_num += 1
        if line_num < (len(query_parts)):
            # Anything other than the last line we add a comma
            query += ",\n"
        else:
            query += "\n"
    query += "]}"                          # Finish the ANDing
 
    return(query)
        
#-------------------------------------------------------------------------------
# Runs the query. Converts the JSON query into a dictionary and 
# runs it against the MongoDB database.
def run_query(collection, query):

    if query == '':
        # Return everything
        raw_results   = collection.find()
    else:
        # Convert JSON string to a dictionary and run query
        jsonquery = json.loads(query)
        raw_results   = collection.find(jsonquery)

    count = 0
    final_results = []
    for doc in raw_results:
        newdoc      = {}    
        count      += 1
        # Copy all the key/value pairs into the new document
        for key,value in doc.items():
            if key != '_id':
                newdoc[key] = value

        # Append this new document to the output
        final_results.append(newdoc)

    return(count, final_results)


    collection = mongo_connect("FarahKKhan", "Birkbeck2", "cluster0.p1f7xxu.mongodb.net",
                           "/", "Cluster0", "AntibodyBasedDrugs")

    # Once you have a 'collection' variable (for your connection with the
    # MongoDB database) you can call run_query() against the database
    (n_results, results) = run_query(collection, query)

    # Iterate over the returned entries
    for result in results:
        # In reality you need to do something here to start a row in your HTML table

        # Iterate over the key/value pairs
        for key,value in result.items():
            # Here you would test for the keys of interest that you want to use in the summary
            # table and print the html table data for those
            if (len(key)):
                print(key + ':' + value)




collection = mongo_connect("FarahKKhan", "Birkbeck2", "cluster0.p1f7xxu.mongodb.net",
                           "/", "Cluster0", "AntibodyBasedDrugs")
                       

# Grab the form and the 'source' button value
# form  = cgi.FieldStorage()
# value = form.getvalue('source')

"""

Example of how you handle the yes/no/don't care buttons

Obviously, add_to_query(), combine_query_parts(), and run_query() are the routines
you have been using previously.

"""


# A list of the Yes/No/Don't care buttons' names in the HTML
yes_no_buttons = ['conj',
                  'bispecific',
                  'fusion',
                  'hc_pot_n-linked',
                  'hc_con_n-linked',
                  'lc_pot_n-linked',
                  'lc_con_n-linked',
                  'hc_pot_o-linked',
                  'hc_con_o-linked',
                  'lc_pot_o-linked',
                  'lc_con_o-linked',
                  'hc_avoid_free_thiol',
                  'hc_artificial_disulfide',
                  'hc_bispecific_formation',
                  'hc_bispecific_formation_with_light_chain',
                  'hc_change_isoelectric_point',
                  'hc_cloning',
                  'hc_conjugation_site',
                  'hc_controlled_Fab-arm_exchange',
                  'hc_disulfide',
                  'hc_disulfide_with_CL',
                  'hc_disulfide_with_H',
                  'hc_disulfide_with_Heavy',
                  'hc_disulfide_with_L',
                  'hc_disulfides_with_light_chain',
                  'hc_eliminate_C1q_binding',
                  'hc_Enforce_pairing',
                  'hc_Enhance_ADCC, Enhance_CD16_binding',
                  'hc_enhance-Fc-effector_functions_and_eliminate_complement_binding',
                  'hc_enhance_FcGamma-RIIB_binding',
                  'hc_enhance_FcRn_binding',
                  'hc_enhancing_CD16A_binding',
                  'hc_extend_half-life',
                  'hc_extend_half_life',
                  'hc_heterodimer_formation',
                  'hc_heterodimer_formation_hole',
                  'hc_heterodimer_formation_knob',
                  'hc_heterodimer_knob_hole',
                  'hc_hexabody_formation',
                  'hc_hexamer_formation',
                  'hc_hinge_stabilization',
                  'hc_improve_affinity',
                  'hc_increase_stability',
                  'hc_match_last_2_residues_VH',
                  'hc_prevent_FcGammaR_binding',
                  'hc_prevent_oxidation',
                  'hc_Protein_A_binding',
                  'hc_Reduce_ADCC',
                  'hc_Reduce_ADCC_and_CDC',
                  'hc_reduce_ADCC_and_CDC',
                  'hc_Reduce_ADCC,_CDC_and_ADCP',
                  'hc_reduce_aggregation_and_modulate_affinity',
                  'hc_Reduce_C1q_binding',
                  'hc_Reduce_CDC',
                  'hc_reduce_deamidation',
                  'hc_reduce_FcRn_binding',
                  'hc_reduce_FcGammaR_binding',
                  'hc_reduce_FcGammaR_binding,_matches_IgG2*02',
                  'hc_reduce_FcGammaR_and_C1q_binding',
                  'hc_reduce_FcGammaR_and_C1q_binding,_reduce_antibody-dependent_disease_enhancement',
                  'hc_reduce_Protein_A_binding',
                  'hc_reduce_proteolysis',
                  'hc_retain_only_FcGamma-RIIB_binding',
                  'hc_remove_CHS',
                  'hc_remove_disulfide',
                  'hc_remove_glycosylation_site',
                  'hc_remove_unpaired_cysteine',
                  'hc_remove_unpaired_sulfhydryl_group',
                  'hc_stabilization_at_low_pH',
                  'hc_TM_reduce_antibody-dependent_disease_enhancement',
                  'hc_transferrin_receptor_binding_epitope',
                  'hc_unpairs_LC_cys_for_conjugation_site',
                  'lc_bispecific_formation',
                  'lc_bispecific_formation_with_heavy_chain',
                  'lc_change_disulfide_with_CL',
                  'lc_disulfide',
                  'lc_disulfides_with_heavy_chain',
                  'lc_Enforce_pairing',
                  'lc_match_first_2_residues_of_CH1_IGHG1*01',
                  'lc_prevent_deamidation',
                  'lc_remove_disulphide',
                  'lc_remove_glycosylation_site']

# A list of the multi-value buttons (i.e. not just yes/no and the word MUST appear)
multi_value_buttons = ['Source_of_the_antibody', 
                       'Antibody_type_Heavy_Chain', 
                       'Antibody_type_Light_Chain', 
                       'Special_format_chains',
                       'Heavy_Chain_Confirmed_PTM',
                       'Light_Chain_Confirmed_PTM',
                       'CDRs_Source_for_humanized_antibodies']

# A list of buttons where we simply require the keyword to appear (or not appear)
# in the JSON, but don't care about the value (you don't have this at the moment in your HTML)
no_value_buttons = ['has_mutation']

# A list of buttons where we are searching for a specific piece of text within a field and where
# we have a whole set of buttons searching the same field for different pieces of text

#So you have a "list of dictionaries of lists". The first item in this example is:
#'hc_Enhance_ADCC':['MutationH', 'Enhance ADCC'],
#'hc_Enhance_ADCC' is the button name
#'MutationH' is the field to search
#'Enhance ADCC' is the value for which we are searching

alternative_value_buttons = {'hc_Enhance_ADCC':['MutationH', 'Enhance ADCC'],
                             'hc_Reduce_ADCC':['MutationH', 'Reduce ADCC'],
                             'hc_avoid_free_thiol':['MutationH', 'avoid free thiol'],
                             'hc_artificial_disulfide':['MutationH', 'artificial disulfide'],
                             'hc_bispecific_formation':['MutationH', 'bispecific formation'],
                             'hc_bispecific_formation_with_light_chain':['MutationH', 'bispecific formation with light chain'],
                             'hc_change_isoelectric_point':['MutationH', 'change isoelectric point'],
                             'hc_cloning':['MutationH', 'cloning'],
                             'hc_conjugation_site':['MutationH', 'conjugation site'],
                             'hc_controlled_Fab-arm_exchange':['MutationH', 'controlled Fab-arm exchange'],
                             'hc_disulfide':['MutationH', 'disulfide'],
                             'hc_disulfide_with_CL':['MutationH', 'disulfide with CL'],
                             'hc_disulfide_with_H':['MutationH', 'disulfide with H'],
                             'hc_disulfide_with_Heavy':['MutationH', 'disulfide with Heavy'],
                             'hc_disulfide_with_L':['MutationH', 'disulfide with L'],
                             'hc_disulfides_with_light_chain':['MutationH', 'disulfides with light chain'],
                             'hc_eliminate_C1q_binding':['MutationH', 'eliminate C1q binding'],
                             'hc_Enforce_pairing':['MutationH', 'Enforce pairing'],
                             'hc_Enhance_ADCC, Enhance_CD16_binding':['MutationH', 'Enhance ADCC, Enhance CD16 binding'],
                             'hc_enhance-Fc-effector_functions_and_eliminate_complement_binding':['MutationH', 'enhance Fc-effector functions and eliminate complement binding'],
                             'hc_enhance_FcGamma-RIIB_binding':['MutationH', 'enhance FcGamma-RIIB binding'],
                             'hc_enhance_FcRn_binding':['MutationH', 'enhance FcRn binding'],
                             'hc_enhancing_CD16A_binding':['MutationH', 'enhancing CD16A binding'],
                             'hc_extend_half-life':['MutationH', 'extend half-life'],
                             'hc_extend_half_life':['MutationH', 'extend half life'],
                             'hc_heterodimer_formation':['MutationH', 'heterodimer formation'],
                             'hc_heterodimer_formation_hole':['MutationH', 'heterodimer formation hole'],
                             'hc_heterodimer_formation_knob':['MutationH', 'heterodimer formation knob'],
                             'hc_heterodimer_knob_hole':['MutationH', 'heterodimer knob hole'],
                             'hc_hexabody_formation':['MutationH', 'hexabody formation'],
                             'hc_hexamer_formation':['MutationH', 'hexamer formation'],
                             'hc_hinge_stabilization':['MutationH', 'hinge stabilization'],
                             'hc_improve_affinity':['MutationH', 'improve affinity'],
                             'hc_increase_stability':['MutationH', 'increase stability'],
                             'hc_match_last_2_residues_VH':['MutationH', 'match last 2 residues VH'],
                             'hc_prevent_FcGammaR_binding':['MutationH', 'prevent FcGammaR binding'],
                             'hc_prevent_oxidation':['MutationH', 'prevent oxidation'],
                             'hc_Protein_A_binding':['MutationH', 'prevent Protein A binding'],
                             'hc_Reduce_ADCC':['MutationH', 'Reduce ADCC'],
                             'hc_Reduce_ADCC_and_CDC':['MutationH', 'Reduce ADCC and CDC'],
                             'hc_reduce_ADCC_and_CDC':['MutationH', 'reduce ADCC and CDC'],
                             'hc_Reduce_ADCC,_CDC_and_ADCP':['MutationH', 'Reduce ADCC, CDC and ADCP'],
                             'hc_reduce_aggregation_and_modulate_affinity':['MutationH', 'reduce aggregation and modulate affinity'],
                             'hc_Reduce_C1q_binding':['MutationH', 'Reduce C1q binding'],
                             'hc_Reduce_CDC':['MutationH', 'Reduce CDC'],
                             'hc_reduce_deamidation':['MutationH', 'reduce deamidation'],
                             'hc_reduce_FcRn_binding':['MutationH', 'reduce FcRn binding'],
                             'hc_reduce_FcGammaR_binding':['MutationH', 'reduce FcGammaR binding'],
                             'hc_reduce_FcGammaR_binding,_matches_IgG2*02':['MutationH', 'reduce FcGammaR binding, matches IgG2*02'],
                             'hc_reduce_FcGammaR_and_C1q_binding':['MutationH', 'reduce FcGammaR and C1q binding'],
                             'hc_reduce_FcGammaR_and_C1q_binding,_reduce_antibody-dependent_disease_enhancement':['MutationH', 'reduce FcGammaR and C1q binding, reduce antibody-dependent disease enhancement'],
                             'hc_reduce_Protein_A_binding':['MutationH', 'reduce Protein A binding'],
                             'hc_reduce_proteolysis':['MutationH', 'reduce proteolysis'],
                             'hc_retain_only_FcGamma-RIIB_binding':['MutationH', 'retain only FcGamma-RIIB binding'],
                             'hc_remove_CHS':['MutationH', 'remove CHS'],
                             'hc_remove_disulfide':['MutationH', 'remove disulfide'],
                             'hc_remove_glycosylation_site':['MutationH', 'remove glycosylation site'],
                             'hc_remove_unpaired_cysteine':['MutationH', 'remove unpaired cysteine'],
                             'hc_remove_unpaired_sulfhydryl_group':['MutationH', 'remove unpaired sulfhydryl group'],
                             'hc_stabilization_at_low_pH':['MutationH', 'stabilization at low pH'],
                             'hc_TM_reduce_antibody-dependent_disease_enhancement':['MutationH', 'TM reduce antibody-dependent disease enhancement'],
                             'hc_transferrin_receptor_binding_epitope':['MutationH', 'transferrin receptor binding epitope'],
                             'hc_unpairs_LC_cys_for_conjugation_site':['MutationH', 'unpairs LC cys for conjugation site'],
                             'lc_bispecific_formation':['MutationL', 'bispecific formation'],
                             'lc_bispecific_formation_with_heavy_chain':['MutationL', 'bispecific formation with heavy chain'],
                             'lc_change_disulfide_with_CL':['MutationL', 'change disulfide with CL'],
                             'lc_disulfide':['MutationL', 'disulfide'],
                             'lc_disulfides_with_heavy_chain':['MutationL', 'disulfides with heavy chain'],
                             'lc_Enforce_pairing':['MutationL', 'Enforce pairing'],
                             'lc_match_first_2_residues_of_CH1_IGHG1*01':['MutationL', 'match first 2 residues of CH1 IGHG1*01'],
                             'lc_prevent_deamidation':['MutationL', 'prevent deamidation'],
                             'lc_remove_disulphide':['MutationL', 'remove disulphide'],
                             'lc_remove_glycosylation_site':['MutationL', 'remove glycosylation site']}

# A dictionary mapping the button name to the field we need to search
fields = {'conj':'Format',
          'bispecific':'Format',
          'fusion':'Format',
          'Source_of_the_antibody':'Format',
          'Antibody_type_Heavy_Chain':'Type', 
          'Antibody_type_Light_Chain':'Type',
          'Special_format_chains':'Type',
          'hc_pot_n-linked':'HeavyPotentialNGlycos',
          'hc_con_n-linked':'HeavyConfirmedNGlycos',
          'lc_pot_n-linked':'LightPotentialNGlycos',
          'lc_con_n-linked':'LightConfirmedNGlycos',
          'Heavy_Chain_Confirmed_PTM':'HeavyConfirmedPTM',
          'Light_Chain_Confirmed_PTM':'LightConfirmedPTM',
          'hc_avoid_free_thiol':'MutationH',
          'hc_artificial_disulfide':'MutationH',
          'hc_bispecific_formation':'MutationH',
          'hc_bispecific_formation_with_light_chain':'MutationH',
          'hc_change_isoelectric_point':'MutationH',
          'hc_cloning':'MutationH',
          'hc_conjugation_site':'MutationH',
          'hc_controlled_Fab-arm_exchange':'MutationH',
          'hc_disulfide':'MutationH',
          'hc_disulfide_with_CL':'MutationH',
          'hc_disulfide_with_H':'MutationH',
          'hc_disulfide_with_Heavy':'MutationH',
          'hc_disulfide_with_L':'MutationH',
          'hc_disulfides_with_light_chain':'MutationH',
          'hc_eliminate_C1q_binding':'MutationH',
          'hc_Enforce_pairing':'MutationH',
          'hc_Enhance_ADCC, Enhance_CD16_binding':'MutationH',
          'hc_enhance-Fc-effector_functions_and_eliminate_complement_binding':'MutationH',
          'hc_enhance_FcGamma-RIIB_binding':'MutationH',
          'hc_enhance_FcRn_binding':'MutationH',
          'hc_enhancing_CD16A_binding':'MutationH',
          'hc_extend_half-life':'MutationH',
          'hc_extend_half_life':'MutationH',
          'hc_heterodimer_formation':'MutationH',
          'hc_heterodimer_formation_hole':'MutationH',
          'hc_heterodimer_formation_knob':'MutationH',
          'hc_heterodimer_knob_hole':'MutationH',
          'hc_hexabody_formation':'MutationH',
          'hc_hexamer_formation':'MutationH',
          'hc_hinge_stabilization':'MutationH',
          'hc_improve_affinity':'MutationH',
          'hc_increase_stability':'MutationH',
          'hc_match_last_2_residues_VH':'MutationH',
          'hc_prevent_FcGammaR_binding':'MutationH',
          'hc_prevent_oxidation':'MutationH',
          'hc_Protein_A_binding':'MutationH',
          'hc_Reduce_ADCC':'MutationH',
          'hc_Reduce_ADCC_and_CDC':'MutationH',
          'hc_reduce_ADCC_and_CDC':'MutationH',
          'hc_Reduce_ADCC,_CDC_and_ADCP':'MutationH',
          'hc_reduce_aggregation_and_modulate_affinity':'MutationH',
          'hc_Reduce_C1q_binding':'MutationH',
          'hc_Reduce_CDC':'MutationH',
          'hc_reduce_deamidation':'MutationH',
          'hc_reduce_FcRn_binding':'MutationH',
          'hc_reduce_FcGammaR_binding':'MutationH',
          'hc_reduce_FcGammaR_binding,_matches_IgG2*02':'MutationH',
          'hc_reduce_FcGammaR_and_C1q_binding':'MutationH',
          'hc_reduce_FcGammaR_and_C1q_binding,_reduce_antibody-dependent_disease_enhancement':'MutationH',
          'hc_reduce_Protein_A_binding':'MutationH',
          'hc_reduce_proteolysis':'MutationH',
          'hc_retain_only_FcGamma-RIIB_binding':'MutationH',
          'hc_remove_CHS':'MutationH',
          'hc_remove_disulfide':'MutationH',
          'hc_remove_glycosylation_site':'MutationH',
          'hc_remove_unpaired_cysteine':'MutationH',
          'hc_remove_unpaired_sulfhydryl_group':'MutationH',
          'hc_stabilization_at_low_pH':'MutationH',
          'hc_TM_reduce_antibody-dependent_disease_enhancement':'MutationH',
          'hc_transferrin_receptor_binding_epitope':'MutationH',
          'hc_unpairs_LC_cys_for_conjugation_site':'MutationH',
          'has_mutation':'MutationH',
          'lc_bispecific_formation':'MutationL',
          'lc_bispecific_formation_with_heavy_chain':'MutationL',
          'lc_change_disulfide_with_CL':'MutationL',
          'lc_disulfide':'MutationL',
          'lc_disulfides_with_heavy_chain':'MutationL',
          'lc_Enforce_pairing':'MutationL',
          'lc_match_first_2_residues_of_CH1_IGHG1*01':'MutationL',
          'lc_prevent_deamidation':'MutationL',
          'lc_remove_disulphide':'MutationL',
          'lc_remove_glycosylation_site':'MutationL',
          'CDRs_Source_for_humanized_antibodies':'CDRSource'}

# A dictionary mapping the button name to the keyword we will search for
keywords = {'conj':'conjugated',
            'bispecific':'bispecific',
            'fusion':'fusion',
            'hc_pot_n-linked':'NONE',
            'hc_con_n-linked':'NONE',
            'lc_pot_n-linked':'NONE',
            'lc_con_n-linked':'NONE',
            'hc_avoid_free_thiol':'avoid free thiol',
            'hc_artificial_disulfide':'artificial disulfide',
            'hc_bispecific_formation':'bispecific formation',
            'hc_bispecific_formation_with_light_chain':'bispecific formation with light chain',
            'hc_change_isoelectric_point':'change isoelectric point',
            'hc_cloning':'cloning',
            'hc_conjugation_site':'conjugation site',
            'hc_controlled_Fab-arm_exchange':'controlled Fab-arm exchange',
            'hc_disulfide':'disulfide',
            'hc_disulfide_with_CL':'disulfide with CL',
            'hc_disulfide_with_H':'disulfide with H',
            'hc_disulfide_with_Heavy':'disulfide with Heavy',
            'hc_disulfide_with_L':'disulfide with L',
            'hc_disulfides_with_light_chain':'disulfides with light chain',
            'hc_eliminate_C1q_binding':'eliminate C1q binding',
            'hc_Enforce_pairing':'Enforce pairing',
            'hc_Enhance_ADCC, Enhance_CD16_binding':'Enhance ADCC, Enhance CD16 binding',
            'hc_enhance-Fc-effector_functions_and_eliminate_complement_binding':'enhance Fc-effector functions and eliminate complement binding',
            'hc_enhance_FcGamma-RIIB_binding':'enhance FcGamma-RIIB binding',
            'hc_enhance_FcRn_binding':'enhance FcRn binding',
            'hc_enhancing_CD16A_binding':'enhancing CD16A binding',
            'hc_extend_half-life':'extend half-life',
            'hc_extend_half_life':'extend half life',
            'hc_heterodimer_formation':'heterodimer formation',
            'hc_heterodimer_formation_hole':'heterodimer formation hole',
            'hc_heterodimer_formation_knob':'heterodimer formation knob',
            'hc_heterodimer_knob_hole':'heterodimer knob hole',
            'hc_hexabody_formation':'hexabody formation',
            'hc_hexamer_formation':'hexamer formation',
            'hc_hinge_stabilization':'hinge stabilization',
            'hc_improve_affinity':'improve affinity',
            'hc_increase_stability':'increase stability',
            'hc_match_last_2_residues_VH':'match last 2 residues VH',
            'hc_prevent_FcGammaR_binding':'prevent FcGammaR binding',
            'hc_prevent_oxidation':'prevent oxidation',
            'hc_Protein_A_binding':'prevent Protein A binding',
            'hc_Reduce_ADCC':'Reduce ADCC',
            'hc_Reduce_ADCC_and_CDC':'Reduce ADCC and CDC',
            'hc_reduce_ADCC_and_CDC':'reduce ADCC and CDC',
            'hc_Reduce_ADCC,_CDC_and_ADCP':'Reduce ADCC, CDC and ADCP',
            'hc_reduce_aggregation_and_modulate_affinity':'reduce aggregation and modulate affinity',
            'hc_Reduce_C1q_binding':'Reduce C1q binding',
            'hc_Reduce_CDC':'Reduce CDC',
            'hc_reduce_deamidation':'reduce deamidation',
            'hc_reduce_FcRn_binding':'reduce FcRn binding',
            'hc_reduce_FcGammaR_binding':'reduce FcGammaR binding',
            'hc_reduce_FcGammaR_binding,_matches_IgG2*02':'reduce FcGammaR binding, matches IgG2*02',
            'hc_reduce_FcGammaR_and_C1q_binding':'reduce FcGammaR and C1q binding',
            'hc_reduce_FcGammaR_and_C1q_binding,_reduce_antibody-dependent_disease_enhancement':'reduce FcGammaR and C1q binding, reduce antibody-dependent disease enhancement',
            'hc_reduce_Protein_A_binding':'reduce Protein A binding',
            'hc_reduce_proteolysis':'reduce proteolysis',
            'hc_retain_only_FcGamma-RIIB_binding':'retain only FcGamma-RIIB binding',
            'hc_remove_CHS':'remove CHS',
            'hc_remove_disulfide':'remove disulfide',
            'hc_remove_glycosylation_site':'remove glycosylation site',
            'hc_remove_unpaired_cysteine':'remove unpaired cysteine',
            'hc_remove_unpaired_sulfhydryl_group':'remove unpaired sulfhydryl group',
            'hc_stabilization_at_low_pH':'stabilization at low pH',
            'hc_TM_reduce_antibody-dependent_disease_enhancement':'TM reduce antibody-dependent disease enhancement',
            'hc_transferrin_receptor_binding_epitope':'transferrin receptor binding epitope',
            'hc_unpairs_LC_cys_for_conjugation_site':'unpairs LC cys for conjugation site',
            'lc_bispecific_formation':'bispecific formation',
            'lc_bispecific_formation_with_heavy_chain':'bispecific formation with heavy chain',
            'lc_change_disulfide_with_CL':'change disulfide with CL',
            'lc_disulfide':'disulfide',
            'lc_disulfides_with_heavy_chain':'disulfides with heavy chain',
            'lc_Enforce_pairing':'Enforce pairing',
            'lc_match_first_2_residues_of_CH1_IGHG1*01':'match first 2 residues of CH1 IGHG1*01',
            'lc_prevent_deamidation':'prevent deamidation',
            'lc_remove_disulphide':'remove disulphide',
            'lc_remove_glycosylation_site':'remove glycosylation site'}

# Initialize the list of things we will query on
query_parts = []

# Print the output page
print ("Content-Type: text/html\n")

# Obtain the information from the form
form = cgi.FieldStorage()

# Step through the yes/no buttons
for button in yes_no_buttons:
    value = form.getvalue(button)
    if(value is not None and value != "don't care"):
        print(fields[button] + ' ' + keywords[button])
        query_parts = add_to_query(query_parts, fields[button], keywords[button], value)
        #             The field name            ^^^ 
        #             The word we are looking for               ^^^
        #             We know it isn't "don't care", so it must be yes or no      ^^^

        
# Where we have other values which must be in the search we can work in the same way.
for button in multi_value_buttons:
    value = form.getvalue(button)
    if(value is not None and value != "don't care"):
        query_parts = add_to_query(query_parts, fields[button], value, 'yes')
        #             The field name            ^^^ 
        #             The word we are looking for               ^^^
        #             Must always be yes                                ^^^
        
# Step through no-value buttons (i.e. those where we just need a field to be present
# or absent)
for button in no_value_buttons:
    value = form.getvalue(button)
    if(value is not None and value != "don't care"):
        query_parts = add_to_query(query_parts, fields[button], '', value)
        #             The field name            ^^^ 
        #             The word we are looking for (blank)       ^^^
        #             It isn't "don't care", must be yes or no      ^^^

# Step through the alternative_value_buttons where we have multiple buttons using the
# same field, but looking for different pieces of text
for button in alternative_value_buttons:
    value = form.getvalue(button)
    if(value is not None and value != "don't care"):
        query_parts = add_to_query(query_parts,
                                   alternative_value_buttons[button][0],
                                   alternative_value_buttons[button][1], value)
        
query   = combine_query_parts(query_parts)
(n_results, results) = run_query(collection, query)


# Construct some HTML
html = "<html>\n"
html += "  <head>\n"
html += "    <title>Result</title>\n"
html += "  </head>\n"
html += "  <body>\n"
html += "    <h1>Result</h1>\n"
html += "    <pre>\n"

# Iterate over the returned entries
for result in results:
    # In reality you need to do something here to start a row in your HTML table

    # Iterate over the key/value pairs
 for key,value in result.items():
        # Here you would test for the keys of interest that you want to use in the summary
        # table and print the html table data for those
        if (len(key)):
            html += key + ':' + value + "\n"
html += "    </pre>\n"
html += "    <p>\n";
html += "      Number of hits: " + str(n_results) + "\n";
html += "    </p>\n";
html += "  </body>\n"
html += "</html>\n"


# The next two lines strip out any non-standard characters
html = html.encode('ascii', errors='ignore');
html = html.decode()
print (html)
