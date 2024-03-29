<html>
  
<body>
<div class='content'>
<h1><center>Antibodies Database</centre></h1>
<center>The Antibodies Database allows users access to search the database according to the different features of the antibodies</centre></>
      
<form action='/dummy_data.cgi' method='get'>
<p> Search the features of the antibodies below:

<p><b>Identifier (INN "Request Number"):</b><br />
<input name='Request' type='text' size='20' /></p>


<p><b>Source of the antibody:</b><br /></p>
<p><b>Select one or more (in case of more than one source):</b><br />
<input name='Source_of_the_antibody' type='checkbox' value='canine' />canine<br />
<input name='Source_of_the_antibody' type='checkbox' value='caninized' />caninized<br />
<input name='Source_of_the_antibody' type='checkbox' value='chimeric' />chimeric<br />
<input name='Source_of_the_antibody' type='checkbox' value='felinized' />felinized<br />
<input name='Source_of_the_antibody' type='checkbox' value='human' />human<br />
<input name='Source_of_the_antibody' type='checkbox' value='humanized' />humanized<br />
<input name='Source_of_the_antibody' type='checkbox' value='llama' />llama<br />
<input name='Source_of_the_antibody' type='checkbox' value='mouse' />mouse<br />
<input name='Source_of_the_antibody' type='checkbox' value='murine' />murine<br />
<input name='Source_of_the_antibody' type='checkbox' value='rat' />rat<br />
<input name='Source_of_the_antibody' type='checkbox' value='resurfaced' />resurfaced<br />
<input name='Source_of_the_antibody' type='checkbox' checked='1' value='don't care' />don't care<br />
</select>
</p>


<p><b>Nature of the antibody:</b><br />

<table>
<table border="1">

<tr><td><div class="pcode">conjugated</td>
<td><input type="radio" name="conj" value="yes">yes</td>
<td><input type="radio" name="conj" value="no">no</td>
<td><input type="radio" name="conj" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">bispecific</td>
<td><input type="radio" name="bispecific" value="yes">yes</td>
<td><input type="radio" name="bispecific" value="no">no</td>
<td><input type="radio" name="bispecific" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">fusion</td>
<td><input type="radio" name="fusion" value="yes">yes</td>
<td><input type="radio" name="fusion" value="no">no</td>
<td><input type="radio" name="fusion" checked='1' value="don't care">don't care</div></td>
</tr>

</table>

</p>

<p><b>Fusion with:</b><br />
<input name='Request' type='text' size='49' /></p>

<p><b>Enter ID (e.g. clone name, lab code, etc.):</b><br />
<input name='Request' type='text' size='49' /></p>


<p><b>Antibody type:</b><br /></p>
<p><b>Heavy Chain: (select one or more options:)</b><br />
<input name='Antibody_type_Heavy_Chain' type='checkbox' value='IgG1' />IgG1<br />
<input name='Antibody_type_Heavy_Chain' type='checkbox' value='IgG2' />IgG2<br />
<input name='Antibody_type_Heavy_Chain' type='checkbox' value='IgG3' />IgG3<br />
<input name='Antibody_type_Heavy_Chain' type='checkbox' value='IgG4' />IgG4<br />
<input name='Antibody_type_Heavy_Chain' type='checkbox' value='Fv' />Fv<br />
<input name='Antibody_type_Heavy_Chain' type='checkbox' checked='1' value='don't care' />don't care<br />
</p>

<p><b>Antibody type:</b><br /></p>
<p><b>Light Chain: (select one or more options:)</b><br />
<input name='Antibody_type_Light_Chain' type='checkbox' value='kappa' />kappa<br />
<input name='Antibody_type_Light_Chain' type='checkbox' value='lambda' />lambda<br />
<input name='Antibody_type_Light_Chain' type='checkbox' checked='1' value='don't care' />don't care<br />
</p>


<p><b>Special format chains: (select one as appropriate:)</b><br />
<input name='Special_format_chains' type='radio' value='Crossmab' />Crossmab<br />
<input name='Special_format_chains' type='radio' value='scFv' />scFv<br />
<input name='Special_format_chains' type='radio' value='Fab' />Fab<br />
<input name='Special_format_chains' type='radio' value='scFab' />scFab<br />
<input name='Special_format_chains' type='radio' value='VHFc' />VHFc<br />
<input name='Special_format_chains' type='radio' value='XscFv' />XscFv<br />
<input name='Special_format_chains' type='radio' value='single-domain' />single-domain<br />
<input name='Special_format_chains' type='radio' value='TNFSF10-fragment' />TNFSF10-fragment<br />
<input name='Special_format_chains' type='radio' value='Pseudomonas aeruginosa Type III secretion protein PcrV' />Pseudomonas aeruginosa Type III secretion protein PcrV<br />
<input name='Special_format_chains' type='radio' value='hinge' />hinge<br />
<input name='Special_format_chains' type='radio' value='VHH' />VHH<br />
<input name='Special_format_chains' type='radio' value='Fc' />Fc<br />
<input name='Special_format_chains' type='radio' value='OTHER' />OTHER<br />
<input name='Special_format_chains' type='radio' checked='1' value='do not care' />do not care<br />
</p>


<p><b>Name of the antigen:</b><br />
<input name='Request' type='text' size='20' /></p>


<p><b>PTMs:</b><br /></p>

<p><b>Heavy Chain:</b><br />


<table>
<table border="1">
<tr><td><div class="pcode">potential N-linked glycosylation sites</td>
<td><input type="radio" name="hc_pot_n-linked" value="yes">yes</td>
<td><input type="radio" name="hc_pot_n-linked" value="no">no</td>
<td><input type="radio" name="hc_pot_n-linked" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">confirmed N-linked glycosylation sites</td>
<td><input type="radio" name="hc_con_n-linked" value="yes">yes</td>
<td><input type="radio" name="hc_con_n-linked" value="no">no</td>
<td><input type="radio" name="hc_con_n-linked" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">potential O-linked glycosylation sites</td>
<td><input type="radio" name="hc_pot_o-linked" value="yes">yes</td>
<td><input type="radio" name="hc_pot_o-linked" value="no">no</td>
<td><input type="radio" name="hc_pot_o-linked" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">confirmed O-linked glycosylation sites</td>
<td><input type="radio" name="hc_con_o-linked" value="yes">yes</td>
<td><input type="radio" name="hc_con_o-linked" value="no">no</td>
<td><input type="radio" name="hc_con_o-linked" checked='1' value="don't care">don't care</div></td>
</tr>

</table>

</p>


<p><b>Heavy Chain Confirmed PTM:</b><br />
<b>Select one as appropriate:</b><br />
<input name='Heavy_Chain_Confirmed_PTM' type='radio' value='amidation' />amidation<br />
<input name='Heavy_Chain_Confirmed_PTM' type='radio' value='cterclip' />cterclip<br />
<input name='Heavy_Chain_Confirmed_PTM' type='radio' value='deamidation' />deamidation<br />
<input name='Heavy_Chain_Confirmed_PTM' type='radio' value='glycation' />glycation<br />
<input name='Heavy_Chain_Confirmed_PTM' type='radio' value='hydroxylation' />hydroxylation<br />
<input name='Heavy_Chain_Confirmed_PTM' type='radio' value='isomerization' />isomerization<br />
<input name='Heavy_Chain_Confirmed_PTM' type='radio' value='nterdeformylate' />nterdeformylate<br />
<input name='Heavy_Chain_Confirmed_PTM' type='radio' value='nterpca' />nterpca<br />
<input name='Heavy_Chain_Confirmed_PTM' type='radio' value='oxidation' />oxidation<br />
<input name='Heavy_Chain_Confirmed_PTM' type='radio' value='succinide-formation' />succinide-formation<br />
<input name='Heavy_Chain_Confirmed_PTM' type='radio' value='succinimide-formation' />succinimide-formation<br />
<input name='Heavy_Chain_Confirmed_PTM' type='radio' checked='1' value='do not care' />do not care<br />
</p>


<p><b>Germline Assignment:</b><br />

<p><b>germline assignment for variable fragment:</b><br />
<input name='Request' type='text' size='49' /></p>

<p><b>germline assignment for joining fragment:</b><br />
<input name='Request' type='text' size='49' /></p>

<p><b>germline assignment for constant fragment:</b><br />
<input name='Request' type='text' size='49' /></p>




<p><b>PTMs:</b><br /></p>

<p><b>Light Chain:</b><br />
<table>
<table border="1">
<tr><td><div class="pcode">potential N-linked glycosylation sites</td>
<td><input type="radio" name="lc_pot_n-linked" value="yes">yes</td>
<td><input type="radio" name="lc_pot_n-linked" value="no">no</td>
<td><input type="radio" name="lc_pot_n-linked" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">confirmed N-linked glycosylation sites</td>
<td><input type="radio" name="lc_con_n-linked" value="yes">yes</td>
<td><input type="radio" name="lc_con_n-linked" value="no">no</td>
<td><input type="radio" name="lc_con_n-linked" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">potential O-linked glycosylation sites</td>
<td><input type="radio" name="lc_pot_o-linked" value="yes">yes</td>
<td><input type="radio" name="lc_pot_o-linked" value="no">no</td>
<td><input type="radio" name="lc_pot_o-linked" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">confirmed O-linked glycosylation sites</td>
<td><input type="radio" name="lc_con_o-linked" value="yes">yes</td>
<td><input type="radio" name="lc_con_o-linked" value="no">no</td>
<td><input type="radio" name="lc_con_o-linked" checked='1' value="don't care">don't care</div></td>
</tr>

</table>

</p>

<p><b>Light Chain Confirmed PTM:</b><br />
<b>Select one as appropriate:</b><br />
<select name='foo' size='1' multiple='1'>
<option>cterclip</option>
<option>deamidation</option>
<option>glycation</option>
<option>isomerization</option>
<option>nterpca</option>
<option>nterdeformylate</option>
<option>oxidation</option>
</select>
</p>

<p><b>Light Chain Confirmed PTM:</b><br />
<b>Select one as appropriate:</b><br />
<input name='Light_Chain_Chain_Confirmed_PTM' type='radio' value='cterclip' />cterclip<br />
<input name='Light_Chain_Confirmed_PTM' type='radio' value='deamidation' />deamidation<br />
<input name='Light_Chain_Confirmed_PTM' type='radio' value='glycation' />glycation<br />
<input name='Light_Chain_Confirmed_PTM' type='radio' value='isomerization' />isomerization<br />
<input name='Light_Chain_Chain_Confirmed_PTM' type='radio' value='nterpca' />nterpca<br />
<input name='Light_Chain_Confirmed_PTM' type='radio' value='nterdeformylate' />nterdeformylate<br />
<input name='Light_Chain_Confirmed_PTM' type='radio' value='oxidation' />oxidation<br />
<input name='Light_Chain_Confirmed_PTM' type='radio' checked='1' value='do not care' />do not care<br />
</p>






<p><b>Germline Assignment:</b><br />

<p><b>germline assignment for variable fragment:</b><br />
<input name='Request' type='text' size='49' /></p>

<p><b>germline assignment for joining fragment:</b><br />
<input name='Request' type='text' size='49' /></p>

<p><b>germline assignment for constant fragment:</b><br />
<input name='Request' type='text' size='49' /></p>






<p><b>Purpose of mutations:</b><br /></p>

<p><b>Heavy Chain:</b><br />

<table>
<table border="1">
<tr><td><div class="pcode">436-488 now matches IgG3</td>
<td><input type="radio" name="hc_436-488" value="yes">yes</td>
<td><input type="radio" name="hc_436-488" value="no">no</td>
<td><input type="radio" name="hc_436-488" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">avoid free thiol</td>
<td><input type="radio" name="hc_avoid_free_thiol" value="yes">yes</td>
<td><input type="radio" name="hc_avoid_free_thiol" value="no">no</td>
<td><input type="radio" name="hc_avoid_free_thiol" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">artificial disulfide</td>
<td><input type="radio" name="hc_artificial_disulfide" value="yes">yes</td>
<td><input type="radio" name="hc_artificial_disulfide" value="no">no</td>
<td><input type="radio" name="hc_artificial_disulfide" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">bispecific formation</td>
<td><input type="radio" name="hc_bispecific_formation" value="yes">yes</td>
<td><input type="radio" name="hc_bispecific_formation" value="no">no</td>
<td><input type="radio" name="bispecific_formation" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">bispecific formation with light chain</td>
<td><input type="radio" name="hc_bispecific_formation_with_light_chain" value="yes">yes</td>
<td><input type="radio" name="hc_bispecific_formation_with_light_chain" value="no">no</td>
<td><input type="radio" name="hc_bispecific_formation_with_light_chain" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">change isoelectric point</td>
<td><input type="radio" name="hc_change isoelectric_point" value="yes">yes</td>
<td><input type="radio" name="hc_change isoelectric_point" value="no">no</td>
<td><input type="radio" name="hc_change isoelectric_point" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">cloning</td>
<td><input type="radio" name="hc_cloning" value="yes">yes</td>
<td><input type="radio" name="hc_cloning" value="no">no</td>
<td><input type="radio" name="hc_cloning" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">conjugation site</td>
<td><input type="radio" name="hc_conjugation_site" value="yes">yes</td>
<td><input type="radio" name="hc_conjugation_site" value="no">no</td>
<td><input type="radio" name="hc_conjugation_site" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">controlled Fab-arm exchange</td>
<td><input type="radio" name="hc_controlled_Fab-arm_exchange" value="yes">yes</td>
<td><input type="radio" name="hc_controlled_Fab-arm_exchange" value="no">no</td>
<td><input type="radio" name="hc_controlled_Fab-arm_exchange" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">disulfide</td>
<td><input type="radio" name="hc_disulfide" value="yes">yes</td>
<td><input type="radio" name="hc_disulfide" value="no">no</td>
<td><input type="radio" name="hc_disulfide" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">disulfide with CL</td>
<td><input type="radio" name="hc_disulfide_with_CL" value="yes">yes</td>
<td><input type="radio" name="hc_disulfide_with_CL" value="no">no</td>
<td><input type="radio" name="hc_disulfide_with_CL" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">disulfide with H[1]</td>
<td><input type="radio" name="hc_disulfide_with_H[1]" value="yes">yes</td>
<td><input type="radio" name="hc_disulfide_with_H[1]" value="no">no</td>
<td><input type="radio" name="hc_disulfide_with_H[1]" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">disulfide with H[2]</td>
<td><input type="radio" name="hc_disulfide_with_H[2]" value="yes">yes</td>
<td><input type="radio" name="hc_disulfide_with_H[2]" value="no">no</td>
<td><input type="radio" name="hc_disulfide_with_H[2]" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">disulfide with Heavy[1]</td>
<td><input type="radio" name="hc_disulfide_with_Heavy[1]" value="yes">yes</td>
<td><input type="radio" name="hc_disulfide_with_Heavy[1]" value="no">no</td>
<td><input type="radio" name="hc_disulfide_with_Heavy[1]" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">disulfide with Heavy[3]</td>
<td><input type="radio" name="hc_disulfide_with_Heavy[3]" value="yes">yes</td>
<td><input type="radio" name="hc_disulfide_with_Heavy[3]" value="no">no</td>
<td><input type="radio" name="hc_disulfide_with_Heavy[3]" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">disulfide with L[2]</td>
<td><input type="radio" name="hc_disulfide_with_L[2]" value="yes">yes</td>
<td><input type="radio" name="hc_disulfide_with_L[2]" value="no">no</td>
<td><input type="radio" name="hc_disulfide_with_L[2]" checked='1' value="don't care">don't care</div></td>
</tr

<tr><td><div class="pcode">disulfides with light chain</td>
<td><input type="radio" name="hc_disulfides_with_light_chain" value="yes">yes</td>
<td><input type="radio" name="hc_disulfides_with_light_chain" value="no">no</td>
<td><input type="radio" name="hc_disulfides_with_light_chain" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">eliminate C1q binding</td>
<td><input type="radio" name="hc_eliminate_C1q_binding" value="yes">yes</td>
<td><input type="radio" name="hc_eliminate_C1q_binding" value="no">no</td>
<td><input type="radio" name="hc_eliminate_C1q_binding" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">Enforce pairing</td>
<td><input type="radio" name="hc_Enforce_pairing" value="yes">yes</td>
<td><input type="radio" name="hc_Enforce_pairing" value="no">no</td>
<td><input type="radio" name="hc_Enforce_pairing" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">Enhance ADCC, Enhance CD16 binding</td>
<td><input type="radio" name="hc_Enhance_ADCC, Enhance_CD16_binding" value="yes">yes</td>
<td><input type="radio" name="hc_Enhance_ADCC, Enhance_CD16_binding" value="no">no</td>
<td><input type="radio" name="hc_Enhance_ADCC, Enhance_CD16_binding" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">enhance Fc-effector functions and eliminate complement binding</td>
<td><input type="radio" name="hc_enhance-Fc-effector_functions_and_eliminate_complement_binding" value="yes">yes</td>
<td><input type="radio" name="hc_enhance-Fc-effector_functions_and_eliminate_complement_binding" value="no">no</td>
<td><input type="radio" name="hc_enhance-Fc-effector_functions_and_eliminate_complement_binding" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">enhance FcGamma-RIIB binding</td>
<td><input type="radio" name="hc_enhance_FcGamma-RIIB_binding" value="yes">yes</td>
<td><input type="radio" name="hc_enhance_FcGamma-RIIB_binding" value="no">no</td>
<td><input type="radio" name="hc_enhance_FcGamma-RIIB_binding" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">enhance FcRn binding</td>
<td><input type="radio" name="hc_enhance_FcRn_binding" value="yes">yes</td>
<td><input type="radio" name="hc_enhance_FcRn_binding" value="no">no</td>
<td><input type="radio" name="hc_enhance_FcRn_binding" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">enhancing CD16A binding</td>
<td><input type="radio" name="hc_enhancing_CD16A_binding" value="yes">yes</td>
<td><input type="radio" name="hc_enhancing_CD16A_binding" value="no">no</td>
<td><input type="radio" name="hc_enhancing_CD16A_binding" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">extend half-life</td>
<td><input type="radio" name="hc_extend_half-life" value="yes">yes</td>
<td><input type="radio" name="hc_extend_half-life" value="no">no</td>
<td><input type="radio" name="hc_extend_half-life" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">extend half life</td>
<td><input type="radio" name="hc_extend_half_life" value="yes">yes</td>
<td><input type="radio" name="hc_extend_half_life" value="no">no</td>
<td><input type="radio" name="hc_extend_half_life" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">heterodimer formation</td>
<td><input type="radio" name="hc_heterodimer_formation" value="yes">yes</td>
<td><input type="radio" name="hc_heterodimer_formation" value="no">no</td>
<td><input type="radio" name="hc_heterodimer_formation" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">heterodimer formation hole</td>
<td><input type="radio" name="hc_heterodimer_formation_hole" value="yes">yes</td>
<td><input type="radio" name="hc_heterodimer_formation_hole" value="no">no</td>
<td><input type="radio" name="hc_heterodimer_formation_hole" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">heterodimer formation knob</td>
<td><input type="radio" name="hc_heterodimer_formation_knob" value="yes">yes</td>
<td><input type="radio" name="hc_heterodimer_formation_knob" value="no">no</td>
<td><input type="radio" name="hc_heterodimer_formation_knob" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">heterodimer knob hole</td>
<td><input type="radio" name="hc_heterodimer_knob_hole" value="yes">yes</td>
<td><input type="radio" name="hc_heterodimer_knob_hole" value="no">no</td>
<td><input type="radio" name="hc_heterodimer_knob_hole" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">hexabody formation</td>
<td><input type="radio" name="hc_hexabody_formation" value="yes">yes</td>
<td><input type="radio" name="hc_hexabody_formation" value="no">no</td>
<td><input type="radio" name="hc_hexabody_formation" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">hexamer formation</td>
<td><input type="radio" name="hc_hexamer_formation" value="yes">yes</td>
<td><input type="radio" name="hc_hexamer_formation" value="no">no</td>
<td><input type="radio" name="hc_hexamer_formation" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">Hinge stabilization</td>
<td><input type="radio" name="hc_Hinge_stabilization" value="yes">yes</td>
<td><input type="radio" name="hc_Hinge_stabilization" value="no">no</td>
<td><input type="radio" name="hc_Hinge_stabilization" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">hinge stabilization</td>
<td><input type="radio" name="hc_hinge_stabilization" value="yes">yes</td>
<td><input type="radio" name="hc_hinge_stabilization" value="no">no</td>
<td><input type="radio" name="hc_hinge_stabilization" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">improve affinity</td>
<td><input type="radio" name="hc_improve_affinity" value="yes">yes</td>
<td><input type="radio" name="hc_improve_affinity" value="no">no</td>
<td><input type="radio" name="hc_improve_affinity" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">increase stability</td>
<td><input type="radio" name="hc_increase_stability" value="yes">yes</td>
<td><input type="radio" name="hc_increase_stability" value="no">no</td>
<td><input type="radio" name="hc_increase_stability" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">match last 2 residues VH</td>
<td><input type="radio" name="hc_match_last_2_residues_VH" value="yes">yes</td>
<td><input type="radio" name="hc_match_last_2_residues_VH" value="no">no</td>
<td><input type="radio" name="hc_match_last_2_residues_VH" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">prevent FcGammaR binding</td>
<td><input type="radio" name="hc_prevent_FcGammaR_binding" value="yes">yes</td>
<td><input type="radio" name="hc_prevent_FcGammaR_binding" value="no">no</td>
<td><input type="radio" name="hc_prevent_FcGammaR_binding" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">prevent oxidation</td>
<td><input type="radio" name="hc_prevent_oxidation" value="yes">yes</td>
<td><input type="radio" name="hc_prevent_oxidation" value="no">no</td>
<td><input type="radio" name="hc_prevent_oxidation" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">prevent Protein A binding</td>
<td><input type="radio" name="hc_Protein_A_binding" value="yes">yes</td>
<td><input type="radio" name="hc_Protein_A_binding" value="no">no</td>
<td><input type="radio" name="hc_Protein_A_binding" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">Reduce ADCC</td>
<td><input type="radio" name="hc_Reduce_ADCC" value="yes">yes</td>
<td><input type="radio" name="hc_Reduce_ADCC" value="no">no</td>
<td><input type="radio" name="hc_Reduce_ADCC" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">Reduce ADCC and CDC</td>
<td><input type="radio" name="hc_Reduce_ADCC_and_CDC" value="yes">yes</td>
<td><input type="radio" name="hc_Reduce_ADCC_and_CDC" value="no">no</td>
<td><input type="radio" name="hc_Reduce_ADCC_and_CDC" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">reduce ADCC and CDC</td>
<td><input type="radio" name="hc_reduce_ADCC_and_CDC" value="yes">yes</td>
<td><input type="radio" name="hc_reduce_ADCC_and_CDC" value="no">no</td>
<td><input type="radio" name="hc_reduce_ADCC_and_CDC" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">Reduce ADCC, CDC and ADCP</td>
<td><input type="radio" name="hc_Reduce_ADCC,_CDC_and_ADCP" value="yes">yes</td>
<td><input type="radio" name="hc_Reduce_ADCC,_CDC_and_ADCP" value="no">no</td>
<td><input type="radio" name="hc_Reduce_ADCC,_CDC_and_ADCP" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">reduce aggregation and modulate affinity</td>
<td><input type="radio" name="hc_reduce_aggregation_and_modulate_affinity" value="yes">yes</td>
<td><input type="radio" name="hc_reduce_aggregation_and_modulate_affinity" value="no">no</td>
<td><input type="radio" name="hc_reduce_aggregation_and_modulate_affinity" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">Reduce C1q binding</td>
<td><input type="radio" name="hc_Reduce_C1q_binding" value="yes">yes</td>
<td><input type="radio" name="hc_Reduce_C1q_binding" value="no">no</td>
<td><input type="radio" name="hc_Reduce_C1q_binding" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">Reduce CDC</td>
<td><input type="radio" name="hc_Reduce_CDC" value="yes">yes</td>
<td><input type="radio" name="hc_Reduce_CDC" value="no">no</td>
<td><input type="radio" name="hc_Reduce_CDC" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">reduce deamidation</td>
<td><input type="radio" name="hc_reduce_deamidation" value="yes">yes</td>
<td><input type="radio" name="hc_reduce_deamidation" value="no">no</td>
<td><input type="radio" name="hc_reduce_deamidation" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">reduce FcRn binding</td>
<td><input type="radio" name="hc_reduce_FcRn_binding" value="yes">yes</td>
<td><input type="radio" name="hc_reduce_FcRn_binding" value="no">no</td>
<td><input type="radio" name="hc_reduce_FcRn_binding" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">reduce FcGammaR binding</td>
<td><input type="radio" name="hc_reduce_FcGammaR_binding" value="yes">yes</td>
<td><input type="radio" name="hc_reduce_FcGammaR_binding" value="no">no</td>
<td><input type="radio" name="hc_reduce_FcGammaR_binding" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">reduce FcGammaR binding, matches IgG2*02</td>
<td><input type="radio" name="hc_reduce_FcGammaR_binding,_matches_IgG2*02" value="yes">yes</td>
<td><input type="radio" name="hc_reduce_FcGammaR_binding,_matches_IgG2*02" value="no">no</td>
<td><input type="radio" name="hc_reduce_FcGammaR_binding,_matches_IgG2*02" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">reduce FcGammaR and C1q binding</td>
<td><input type="radio" name="hc_reduce_FcGammaR_and_C1q_binding" value="yes">yes</td>
<td><input type="radio" name="hc_reduce_FcGammaR_and_C1q_binding" value="no">no</td>
<td><input type="radio" name="hc_reduce_FcGammaR_and_C1q_binding" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">reduce FcGammaR and C1q binding, reduce antibody-dependent disease enhancement</td>
<td><input type="radio" name="hc_reduce_FcGammaR_and_C1q_binding,_reduce_antibody-dependent_disease_enhancement" value="yes">yes</td>
<td><input type="radio" name="hc_reduce_FcGammaR_and_C1q_binding,_reduce_antibody-dependent_disease_enhancement" value="no">no</td>
<td><input type="radio" name="hc_reduce_FcGammaR_and_C1q_binding,_reduce_antibody-dependent_disease_enhancement" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">reduce Protein A binding</td>
<td><input type="radio" name="hc_reduce_Protein_A_binding" value="yes">yes</td>
<td><input type="radio" name="hc_reduce_Protein_A_binding" value="no">no</td>
<td><input type="radio" name="hc_reduce_Protein_A_binding" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">reduce proteolysis</td>
<td><input type="radio" name="hc_reduce_proteolysis" value="yes">yes</td>
<td><input type="radio" name="hc_reduce_proteolysis" value="no">no</td>
<td><input type="radio" name="hc_reduce_proteolysis" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">retain only FcGamma-RIIB binding</td>
<td><input type="radio" name="hc_retain_only_FcGamma-RIIB_binding" value="yes">yes</td>
<td><input type="radio" name="hc_retain_only_FcGamma-RIIB_binding" value="no">no</td>
<td><input type="radio" name="hc_retain_only_FcGamma-RIIB_binding" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">remove CHS</td>
<td><input type="radio" name="hc_remove_CHS" value="yes">yes</td>
<td><input type="radio" name="hc_remove_CHS" value="no">no</td>
<td><input type="radio" name="hc_remove_CHS" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">remove disulfide</td>
<td><input type="radio" name="hc_remove_disulfide" value="yes">yes</td>
<td><input type="radio" name="hc_remove_disulfide" value="no">no</td>
<td><input type="radio" name="hc_remove_disulfide" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">remove glycosylation site</td>
<td><input type="radio" name="hc_remove_glycosylation_site" value="yes">yes</td>
<td><input type="radio" name="hc_remove_glycosylation_site" value="no">no</td>
<td><input type="radio" name="hc_remove_glycosylation_site" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">remove unpaired cysteine</td>
<td><input type="radio" name="hc_remove_unpaired_cysteine" value="yes">yes</td>
<td><input type="radio" name="hc_remove_npaired_cysteine" value="no">no</td>
<td><input type="radio" name="hc_remove_npaired_cysteine" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">remove unpaired sulfhydryl group</td>
<td><input type="radio" name="hc_remove_unpaired_sulfhydryl_group" value="yes">yes</td>
<td><input type="radio" name="hc_remove_npaired_sulfhydryl_group" value="no">no</td>
<td><input type="radio" name="hc_remove_npaired_sulfhydryl_group" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">stabilization at low pH</td>
<td><input type="radio" name="hc_stabilization_at_low_pH" value="yes">yes</td>
<td><input type="radio" name="hc_stabilization_at_low_pH" value="no">no</td>
<td><input type="radio" name="hc_stabilization_at_low_pH" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">TM reduce antibody-dependent disease enhancement</td>
<td><input type="radio" name="hc_TM_reduce_antibody-dependent_disease_enhancement" value="yes">yes</td>
<td><input type="radio" name="hc_TM_reduce_antibody-dependent_disease_enhancement" value="no">no</td>
<td><input type="radio" name="hc_TM_reduce_antibody-dependent_disease_enhancement" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">transferrin receptor binding epitope</td>
<td><input type="radio" name="hc_transferrin_receptor_binding_epitope" value="yes">yes</td>
<td><input type="radio" name="hc_transferrin_receptor_binding_epitope" value="no">no</td>
<td><input type="radio" name="hc_transferrin_receptor_binding_epitope" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">unpairs LC cys for conjugation site</td>
<td><input type="radio" name="hc_unpairs_LC_cys_for_conjugation_site" value="yes">yes</td>
<td><input type="radio" name="hc_unpairs_LC_cys_for_conjugation_site" value="no">no</td>
<td><input type="radio" name="hc_unpairs_LC_cys_for_conjugation_site" checked='1' value="don't care">don't care</div></td>
</tr>

</table>

</p>



<p><b>Purpose of mutations:</b><br />


<p><b>Light Chain:</b><br />

<table>
<table border="1">
<tr><td><div class="pcode">bispecific formation</td>
<td><input type="radio" name="lc_bispecific_formation" value="yes">yes</td>
<td><input type="radio" name="lc_bispecific_formation" value="no">no</td>
<td><input type="radio" name="lc_bispecific_formation" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">bispecific formation with heavy chain</td>
<td><input type="radio" name="lc_bispecific_formation_with_heavy_chain" value="yes">yes</td>
<td><input type="radio" name="lc_bispecific_formation_with_heavy_chain" value="no">no</td>
<td><input type="radio" name="lc_bispecific_formation_with_heavy_chain" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">change disulfide with CL</td>
<td><input type="radio" name="lc_change_disulfide_with_CL" value="yes">yes</td>
<td><input type="radio" name="lc_change_disulfide_with_CL" value="no">no</td>
<td><input type="radio" name="lc_change_disulfide_with_CL" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">disulfide</td>
<td><input type="radio" name="lc_disulfide" value="yes">yes</td>
<td><input type="radio" name="lc_disulfide" value="no">no</td>
<td><input type="radio" name="lc_disulfide" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">disulfides with heavy chain</td>
<td><input type="radio" name="lc_disulfides_with_heavy_chain" value="yes">yes</td>
<td><input type="radio" name="lc_disulfides_with_heavy_chain" value="no">no</td>
<td><input type="radio" name="lc_disulfides_with_heavy_chain" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">Enforce pairing</td>
<td><input type="radio" name="lc_Enforce_pairing" value="yes">yes</td>
<td><input type="radio" name="lc_Enforce_pairing" value="no">no</td>
<td><input type="radio" name="lc_Enforce_pairing" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">match first 2 residues of CH1 IGHG1*01</td>
<td><input type="radio" name="lc_match_first_2_residues_of_CH1_IGHG1*01" value="yes">yes</td>
<td><input type="radio" name="lc_match_first_2_residues_of_CH1_IGHG1*01" value="no">no</td>
<td><input type="radio" name="lc_match_first_2_residues_of_CH1_IGHG1*01" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">prevent deamidation</td>
<td><input type="radio" name="lc_prevent_deamidation" value="yes">yes</td>
<td><input type="radio" name="lc_prevent_deamidation" value="no">no</td>
<td><input type="radio" name="lc_prevent_deamidation" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">remove disulphide</td>
<td><input type="radio" name="lc_remove_disulphide" value="yes">yes</td>
<td><input type="radio" name="lc_remove_disulphide" value="no">no</td>
<td><input type="radio" name="lc_remove_disulphide" checked='1' value="don't care">don't care</div></td>
</tr>

<tr><td><div class="pcode">remove glycosylation site</td>
<td><input type="radio" name="lc_remove_glycosylation_site" value="yes">yes</td>
<td><input type="radio" name="lc_remove_glycosylation_site" value="no">no</td>
<td><input type="radio" name="lc_remove_glycosylation_site" checked='1' value="don't care">don't care</div></td>
</tr>

</table>

</p>


<p><b>CDRs Source for humanized antibodies: (select one as appropriate:)</b><br />
<input name='CDRs_Source_for_humanized_antibodies' type='radio' value='camelid' />camelid<br />
<input name='CDRs_Source_for_humanized_antibodies' type='radio' value='Camelus bactrianus' />Camelus bactrianus<br />
<input name='CDRs_Source_for_humanized_antibodies' type='radio' value='Homo sapiens' />Homo sapiens<br />
<input name='CDRs_Source_for_humanized_antibodies' type='radio' value='Homo sapiens (MeMo mouse)' />Homo sapiens (MeMo mouse)<br />
<input name='CDRs_Source_for_humanized_antibodies' type='radio' value='Homo sapiens (phage library from immunized MeMo mouse)' />Homo sapiens (phage library from immunized MeMo mouse)<br />
<input name='CDRs_Source_for_humanized_antibodies' type='radio' value='human' />human<br />
<input name='CDRs_Source_for_humanized_antibodies' type='radio' value='Immunization of mouse' />Immunization of mouse<br />
<input name='CDRs_Source_for_humanized_antibodies' type='radio' value='Lama glama' />Lama glama<br />
<input name='CDRs_Source_for_humanized_antibodies' type='radio' value='llama' />llama<br />
<input name='CDRs_Source_for_humanized_antibodies' type='radio' value='Mus musculus' />Mus musculus<br />
<input name='CDRs_Source_for_humanized_antibodies' type='radio' value='Mus musculus (plus heavy chain randomization)' />Mus musculus (plus heavy chain randomization)<br />
<input name='CDRs_Source_for_humanized_antibodies' type='radio' value='murine hybridoma' />murine hybridoma<br />
<input name='CDRs_Source_for_humanized_antibodies' type='radio' value='Rattus norvegicus' />Rattus norvegicus<br />
<input name='CDRs_Source_for_humanized_antibodies' type='radio' value='rat' />rat<br />
<input name='CDRs_Source_for_humanized_antibodies' type='radio' value='Oryctolagus cuniculus' />Oryctolagus cuniculus<br />
<input name='CDRs_Source_for_humanized_antibodies' type='radio' value='unknown' />unknown<br />
<input name='CDRs_Source_for_humanized_antibodies' type='radio' checked='1' value='do not care' />do not care<br />
</p>





<p><input type='Submit' value='Search' />
<input type='reset'  value='Clear form' />
</p>

</form>
      
</div>
</body>
</html>


<div class="footer">
         <p><left>MSc Bioinformatics Project</left></p>
        </div>