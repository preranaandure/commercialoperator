<template lang="html">
    <div class="container" >
        <div class="row">
            <div class="col-sm-12">
                <form class="form-horizontal" name="personal_form" method="post">

                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <h3 class="panel-title">Applicant <small>The applicant will be the licensee.</small><i class="fa fa-question-circle" data-toggle="tooltip" data-placement="bottom" style="color:blue" title="Please ensure the applicant is the same as the insured party on your public liability on your public liability insurance certificate.">&nbsp;</i>
                                <a :href="'#'+pBody" data-toggle="collapse"  data-parent="#userInfo" expanded="true" :aria-controls="pBody">
                                    <span class="glyphicon glyphicon-chevron-up pull-right "></span>
                                </a>
                            </h3>
                        </div>
                        <div class="panel-body collapse in" :id="pBody">

                            <div class="col-sm-12">
                                <!-- <label>Do you apply </label> </br> -->
                                <div class="form-group" v-if="!isLoading">
                                    <!-- <div class="radio">
                                        <label>
                                            <input type="radio"  name="behalf_of_org" v-model="org_applicant" value="yourself"> On behalf of yourself
                                        </label>
                                    </div> -->
                                    <div v-if="profile.commercialoperator_organisations.length > 0">
                                        <label>Do you apply </label> 
                                        <br/>
                                        <div v-for="org in profile.commercialoperator_organisations" class="radio">
                                            <label v-if ="!org.is_consultant">
                                              <input type="radio" name="behalf_of_org" v-model="org_applicant"  :value="org.id"> On behalf of {{org.name}}
                                            </label>
                                            <label v-if ="org.is_consultant">
                                              <input type="radio" name="behalf_of_org" v-model="org_applicant"  :value="org.id"> On behalf of {{org.name}} (as a Consultant)
                                            </label>
                                        </div>
                                        <!--
                                        <div class="radio">
                                            <label class="radio-inline">
                                              <input type="radio" name="behalf_of_org" v-model="behalf_of"  value="other" > On behalf of an organisation (as an authorised agent)
                                            </label>
                                        </div>
                                        -->
                                    </div>
                                    <div v-else>
                                        <p style="color:red"> You cannot start a new application as you have not linked yourself to any organisation yet. Please go to your account page in the Options menu to link your self to an organisation.</p>
                                    </div>
                                </div>
                            </div>
                            <!--
                            <div v-if="behalf_of == 'other'" class="col-sm-12">
                                <div class="row">
                                    <div class="form-group col-sm-5">
                                        <label for="" class="control-label">Organisation</label>
                                        <input type="text" class="form-control" name="first_name" placeholder="" v-model="agent.organisation">
                                    </div>
                                    <div class="form-group col-sm-1"></div>
                                    <div class="form-group col-sm-5">
                                        <label for="" class="control-label" >ABN / ACN</label>
                                        <input type="text" class="form-control" name="last_name" placeholder="" v-model="agent.abn">
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="form-group col-sm-5">
                                        <label for="" class="control-label" >Organisation contact given name(s)</label>
                                        <input type="text" class="form-control" name="last_name" placeholder="" v-model="agent.given_names">
                                    </div>
                                    <div class="form-group col-sm-1"></div>
                                    <div class="form-group col-sm-5">
                                        <label for="" class="control-label" >Orgnisation contact surname</label>
                                        <input type="text" class="form-control" name="last_name" placeholder="" v-model="agent.surname">
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="form-group col-sm-5">
                                        <label for="" class="control-label" >Organisation contact email address</label>
                                        <input type="text" class="form-control" name="last_name" placeholder="" v-model="agent.email">
                                    </div>
                                </div>
                            </div>
                            -->
                        </div>
                    </div>

                    <div v-if="org_applicant != ''||yourself!=''" class="panel panel-default">
                        <div class="panel-heading">
                            <h3 class="panel-title">Apply for
                                <a :href="'#'+pBody2" data-toggle="collapse"  data-parent="#userInfo2" expanded="true" :aria-controls="pBody2">
                                    <span class="glyphicon glyphicon-chevron-up pull-right "></span>
                                </a>
                            </h3>
                        </div>
                        <div class="panel-body collapse in" :id="pBody2">
                            <div>
                                <label for="" class="control-label" >Licence Type * <a :href="proposal_type_help_url" target="_blank"><i class="fa fa-question-circle" style="color:blue">&nbsp;</i></a></label>
                                <div class="col-sm-12">
                                    <div class="form-group">
                                        <select class="form-control" style="width:40%" v-model="selected_application_id" @change="chainedSelectAppType(selected_application_id)">
											<option value="" selected disabled>Select Licence type*</option>
                                            <option v-for="application_type in application_types" :value="application_type.value">
                                                {{ application_type.text }}
                                            </option>
                                        </select>
                                    </div>
                                </div>
                            </div>

                            <div class="" v-show="has_event_proposals()">
                                <!-- <p style="color:red;"> An event application already exists in the system: </p>
                                <p style="color:red;"> {{ event_proposals() }}</p> -->
                                <div>
                                    <label for="" class="control-label" >Prefill application with details from previously approved event </label>
                                    <div class="col-sm-12">
                                        <div class="form-group">
                                            <select class="form-control" style="width:40%" v-model="selected_copy_from" >
                                                <option value="" selected disabled>Select Event Licence to copy from*</option>
                                                <option v-for="proposal in event_proposals()" :value="proposal.current_proposal">
                                                    {{ proposal.current_proposal__event_activity__event_name }}
                                                </option>
                                            </select>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div v-if="display_region_selectbox">
                                <label for="" class="control-label" >Region * <a :href="region_help_url" target="_blank"><i class="fa fa-question-circle" style="color:blue">&nbsp;</i></a> </label>
                                <div class="col-sm-12">
                                    <div class="form-group">
                                        <select v-model="selected_region" class="form-control" style="width:40%" @change="chainedSelectDistricts(selected_region)">
											<option value="" selected disabled>Select region</option>
                                            <option v-for="region in regions" :value="region.value">
                                                {{ region.text }}
                                            </option>
                                        </select>
                                    </div>
                                </div>
                            </div> 

                            <div v-if="display_region_selectbox && selected_region">
                                <label for="" class="control-label" style="font-weight: normal;">District <a :href="district_help_url" target="_blank"><i class="fa fa-question-circle" style="color:blue">&nbsp;</i></a></label>
                                <div class="col-sm-12">
                                    <div class="form-group">
                                        <select  v-model="selected_district" class="form-control" style="width:40%">
											<option value="" selected disabled>Select district</option>
                                            <option v-for="district in districts" :value="district.value">
                                                {{ district.text }}
                                            </option>
                                        </select>
                                    </div>
                                </div>
                            </div>

                            <div v-if="display_activity_matrix_selectbox">
								<div v-if="activities.length > 0">
									<label for="" class="control-label" >Activity Type * <a :href="activity_type_help_url" target="_blank"><i class="fa fa-question-circle" style="color:blue">&nbsp;</i></a></label>
									<div class="col-sm-12">
										<div class="form-group">
											<select v-model="selected_activity" @change="chainedSelectSubActivities1(selected_activity)" class="form-control" style="width:40%">
												<option value="" selected disabled>Select activity</option>
												<option v-for="activity in activities" :value="activity.value">
													{{ activity.text }}
												</option>
											</select>
										</div>
									</div>
								</div>

								<div v-if="sub_activities1.length > 0">
									<label for="" class="control-label" >Sub Activity 1 * <a :href="sub_activity_1_help_url" target="_blank"><i class="fa fa-question-circle" style="color:blue">&nbsp;</i></a></label>
									<div class="col-sm-12">
										<div class="form-group">
											<select v-model="selected_sub_activity1" @change="chainedSelectSubActivities2(selected_sub_activity1)" class="form-control" style="width:40%">
												<option value="" selected disabled>Select sub_activity 1</option>
												<option v-for="sub_activity1 in sub_activities1" :value="sub_activity1.value">
													{{ sub_activity1.text }}
												</option>
											</select>
										</div>
									</div>
								</div>

								<div v-if="sub_activities2.length > 0">
									<label for="" class="control-label" >Sub Activity 2 * <a :href="sub_activity_2_help_url" target="_blank"><i class="fa fa-question-circle" style="color:blue">&nbsp;</i></a></label>
									<div class="col-sm-12">
										<div class="form-group">
											<select v-model="selected_sub_activity2" @change="chainedSelectCategories(selected_sub_activity2)" class="form-control" style="width:40%">
												<option value="" selected disabled>Select sub_activity 2</option>
												<option v-for="sub_activity2 in sub_activities2" :value="sub_activity2.value">
													{{ sub_activity2.text }}
												</option>
											</select>
										</div>
									</div>
								</div>

								<div v-if="categories.length > 0">
									<label for="" class="control-label" >Category * <a :href="category_help_url" target="_blank"><i class="fa fa-question-circle" style="color:blue">&nbsp;</i></a></label>
									<div class="col-sm-12">
										<div class="form-group">
											<select v-model="selected_category" @change="get_approval_level(selected_category)" class="form-control" style="width:40%">
												<option value="" selected disabled>Select category</option>
												<option v-for="category in categories" :value="category.value" :name="category.approval">
													{{ category.text }}
												</option>
											</select>
										</div>
									</div>
								</div>
                            </div>

                        </div>
                    </div>

                    <div class="col-sm-12" v-show="has_active_proposals()">
                        <p style="color:red;"> This organisation has a current commercial operations application or licence: You can apply to amend a licence from the licences table on the home dashboard. </p>
                        <p style="color:red;"> {{ active_proposals() }}</p>
                    </div>
                    <!-- <div class="col-sm-12" v-show="has_event_proposals()"> -->
                        <!-- <p style="color:red;"> An event application already exists in the system: </p>
                        <p style="color:red;"> {{ event_proposals() }}</p> -->
                        <!-- <div>
                                <label for="" class="control-label" >Copy from </label>
                                <div class="col-sm-12">
                                    <div class="form-group">
                                        <select class="form-control" style="width:40%" v-model="selected_copy_from" >
                                            <option value="" selected disabled>Select Event Licence to copy from*</option>
                                            <option v-for="proposal in event_proposals()" :value="proposal.current_proposal">
                                                {{ proposal.current_proposal__event_activity__event_name }}
                                            </option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                    </div> -->
                    <div class="col-sm-12">
                        <button v-if="!creatingProposal" :disabled="isDisabled() || has_active_proposals()" @click.prevent="submit()" class="btn btn-primary pull-right">Continue</button>
                        <button v-else disabled class="pull-right btn btn-primary"><i class="fa fa-spin fa-spinner"></i>&nbsp;Creating</button>
                    </div>
                  
                </form>
            </div>
        </div>
    </div>

</template>
<script>
import Vue from 'vue'
import {
  api_endpoints,
  helpers
}
from '@/utils/hooks'
import utils from './utils'
export default {
  data: function() {
    let vm = this;
    return {
        "proposal": null,
        agent: {},
        behalf_of: '',
        org_applicant: '',
        yourself: '',
        profile: {
            commercialoperator_organisations: []
        },
        "loading": [],
        form: null,
        pBody: 'pBody' + vm._uid,
        pBody2: 'pBody2' + vm._uid,

        selected_application_id: '',
        selected_application_name: '',
        selected_region: '',
        selected_district: '',
        application_types: [],
        selected_activity: '',
        selected_sub_activity1: '',
        selected_sub_activity2: '',
        selected_category: '',
        regions: [],
        districts: [],
        activity_matrix: [],
        activities: [],
        sub_activities1: [],
        sub_activities2: [],
        categories: [],
        approval_level: '',
        creatingProposal: false,
        selected_copy_from: null,
        display_region_selectbox: false,
        display_activity_matrix_selectbox: false,
        site_url: (api_endpoints.site_url.endsWith("/")) ? (api_endpoints.site_url): (api_endpoints.site_url + "/"),
    }
  },
  components: {
  },
  computed: {
    isLoading: function() {
      return this.loading.length > 0
    },
    org: function() {
        let vm = this;
        // if (vm.org_applicant != '' || vm.org_applicant != 'submitter'){
        //     return vm.profile.commercialoperator_organisations.find(org => parseInt(org.id) === parseInt(vm.org_applicant)).name;
        // }
        if (vm.org_applicant != '' && vm.org_applicant != 'yourself'){   
            return vm.profile.commercialoperator_organisations.find(org => parseInt(org.id) === parseInt(vm.org_applicant)).name;
        }
        return vm.org_applicant;
    },
    manyDistricts: function() {
      return this.districts.length > 1;
    },
    // proposal_type_help_url: function() {
    //   return this.site_url + "help/commercialoperator/user/#apply_proposal_type"
    // },
    proposal_type_help_url: function() {
      return api_endpoints.proposal_type_help_url;
    },
    region_help_url: function() {
      return this.site_url + "help/commercialoperator/user/#apply_region"
    },
    district_help_url: function() {
      return this.site_url + "help/commercialoperator/user/#apply_district"
    },
    activity_type_help_url: function() {
      return this.site_url + "help/commercialoperator/user/#apply_activity_type"
    },
    sub_activity_1_help_url: function() {
      return this.site_url + "help/commercialoperator/user/#apply_sub_activity_1"
    },
    sub_activity_2_help_url: function() {
      return this.site_url + "help/commercialoperator/user/#apply_sub_activity_2"
    },
    category_help_url: function() {
      return this.site_url + "help/commercialoperator/user/#apply_category"
    },
    application_type_tclass: function(){
        return api_endpoints.t_class;
    },
    application_type_filming: function(){
        return api_endpoints.filming;
    },
    application_type_event: function(){
        return api_endpoints.event;
    },

  },
  methods: {
    has_active_proposals: function() {
        return this.active_proposals().length > 0;
    },
    active_proposals: function() {
        // returns active 'T Class' proposals - cannot have more than 1 active 'T Class' application at a time
        let vm = this;
        var proposals = [];
        var org = vm.profile.commercialoperator_organisations.find(el => el.name === vm.org)
        if (org && vm.selected_application_name == vm.application_type_tclass) {
            proposals = org.active_proposals.find(el => el.application_type === vm.application_type_tclass).proposals
        }
        return proposals;
    },
    has_event_proposals: function() {
        return this.event_proposals().length > 0;
    },
    event_proposals: function() {
        // returns active 'T Class' proposals - cannot have more than 1 active 'T Class' application at a time
        let vm = this;
        var proposals = [];
        var org = vm.profile.commercialoperator_organisations.find(el => el.name === vm.org)
        if (org && vm.selected_application_name == vm.application_type_event) {
            proposals = org.current_event_proposals.find(el => el.application_type === vm.application_type_event).proposals
        }
        return proposals;
    },
    submit: function() {
        let vm = this;
		console.log(vm.org_applicant)
        swal({
            title: "Create " + vm.selected_application_name,
            text: "Are you sure you want to create " + this.alertText() + " application on behalf of "+vm.org+" ?",
            type: "question",
            showCancelButton: true,
            confirmButtonText: 'Accept'
        }).then(() => {
            if (!vm.has_active_proposals()) {
         	    vm.createProposal();
            }
        },(error) => {
        });
    },
    alertText: function() {
        let vm = this;
		if (vm.selected_application_name == vm.application_type_tclass) {
        	//return "a T Class";
            return "a "+vm.application_type_tclass;
		} else if (vm.selected_application_name == vm.application_type_filming) {
        	//return "a Filming";
            return "a "+vm.application_type_filming;
		} else if (vm.selected_application_name == vm.application_type_event) {
        	//return "an Event";
            return "an "+vm.application_type_event;
		}
	},
    createProposal:function () {
        let vm = this;
        vm.creatingProposal = true;
        if(vm.org_applicant=='yourself'){
            vm.org_applicant='';
        }
		vm.$http.post('/api/proposal.json',{
			//behalf_of: vm.behalf_of,
            org_applicant:vm.org_applicant,
			application: vm.selected_application_id,
			region: vm.selected_region,
			district: vm.selected_district,
			//tenure: vm.selected_tenure,
			activity: vm.selected_activity,
            sub_activity1: vm.selected_sub_activity1,
            sub_activity2: vm.selected_sub_activity2,
            category: vm.selected_category,
            approval_level: vm.approval_level,
            selected_copy_from: vm.selected_copy_from,
		}).then(res => {
		    vm.proposal = res.body;
			vm.$router.push({
			    name:"draft_proposal",
				params:{proposal_id:vm.proposal.id}
			});
            vm.creatingProposal = false;
		},
		err => {
			console.log(err);
		});
    },
    isDisabled: function() {
        let vm = this;
        // if (vm.selected_application_name == 'Western Power Maintenance') {
        //     if (vm.behalf_of == '' || vm.selected_application_id == '' || vm.selected_region == '' || vm.approval_level == ''){
        //         return true;
        //     }
        // } else {
        //     if (vm.behalf_of == '' || vm.selected_application_id == ''){
        //         return true;
        //     }
        // }
        if ((vm.org_applicant == '' && vm.yourself=='') ||( vm.selected_application_id == '')){
                return true;
            }
        return false;
    },
	fetchRegions: function(){
		let vm = this;

		vm.$http.get(api_endpoints.regions).then((response) => {
				vm.api_regions = response.body;
				//console.log('api_regions ' + response.body);

                for (var i = 0; i < vm.api_regions.length; i++) {
                    this.regions.push( {text: vm.api_regions[i].name, value: vm.api_regions[i].id, districts: vm.api_regions[i].districts} );
                }
		},(error) => {
			console.log(error);
		})
	},

	searchList: function(id, search_list){
        /* Searches for dictionary in list */
        for (var i = 0; i < search_list.length; i++) {
            if (search_list[i].value == id) {
                return search_list[i];
            }
        }
        return [];
    },
	chainedSelectDistricts: function(region_id){
		let vm = this;
        vm.districts = [];

        var api_districts = this.searchList(region_id, vm.regions).districts;
        if (api_districts.length > 0) {
            for (var i = 0; i < api_districts.length; i++) {
                this.districts.push( {text: api_districts[i].name, value: api_districts[i].id} );
            }
        }
	},
    fetchApplicationTypes: function(){
		let vm = this;

		vm.$http.get(api_endpoints.application_types).then((response) => {
				vm.api_app_types = response.body;
				//console.log('api_app_types ' + response.body);

                for (var i = 0; i < vm.api_app_types.length; i++) {
                    this.application_types.push( {
                        text: vm.api_app_types[i].name, 
                        value: vm.api_app_types[i].id, 
                        //activities: (vm.api_app_types[i].activity_app_types.length > 0) ? vm.api_app_types[i].activity_app_types : [],
                        //tenures: (vm.api_app_types[i].tenure_app_types.length > 0) ? vm.api_app_types[i].tenure_app_types : [],
                    } );
                }
		},(error) => {
			console.log(error);
		})
	},
    chainedSelectAppType: function(application_id){
        /* reset */
		let vm = this;
        vm.selected_region = '';
        vm.selected_district = '';
        vm.selected_activity = '';
        vm.display_region_selectbox = false;
        vm.display_activity_matrix_selectbox = false;
        vm.selected_copy_from= null;

        vm.selected_application_name = this.searchList(application_id, vm.application_types).text
        //this.chainedSelectActivities(application_id);
        //this.chainedSelectActivities(application_id);

        if (vm.selected_application_name == 'Western Power Maintenance') {
            vm.display_region_selectbox = true;
            vm.display_activity_matrix_selectbox = true;
        } 

    },

	fetchActivityMatrix: function(){
		let vm = this;
        vm.sub_activities1 = [];
        vm.sub_activities2 = [];
        vm.categories = [];
        vm.approval_level = '';

		vm.$http.get(api_endpoints.activity_matrix).then((response) => {
				this.activity_matrix = response.body[0].schema[0];
				this.keys_ordered = response.body[0].ordered;
				//console.log('this.activity_matrix ' + response.body[0].schema);

                var keys = this.keys_ordered ? Object.keys(this.activity_matrix).sort() : Object.keys(this.activity_matrix)
                for (var i = 0; i < keys.length; i++) {
                    this.activities.push( {text: keys[i], value: keys[i]} );
                }
		},(error) => {
			console.log(error);
		})
	},
    chainedSelectSubActivities1: function(activity_name){
		let vm = this;
        vm.sub_activities1 = [];
        vm.sub_activities2 = [];
        vm.categories = [];
        vm.selected_sub_activity1 = '';
        vm.selected_sub_activity2 = '';
        vm.selected_category = '';
        vm.approval_level = '';

        vm.sub_activities1 = [];
        var [api_activities, res] = this.get_sub_matrix(activity_name, vm.activity_matrix)
        if (res == "null" || res == null) {
            //for (var i = 0; i < vm.activity_matrix.length; i++) {
            //    if (activity_name == vm.activity_matrix[i]['text']) {
            //        vm.activity_matrix[i]['sub_matrix']
            //    }
            //}
            vm.approval_level = api_activities;
            return;
        } else if (res == "pass") {
            var api_sub_activities = this.get_sub_matrix("pass", api_activities[0])[0];
            if ("pass" in api_sub_activities[0]) {
                // go straight to categories widget
                var categories = api_sub_activities[0]['pass']
                for (var i = 0; i < categories.length; i++) {
                    this.categories.push( {text: categories[i][0], value: categories[i][0], approval: categories[i][1]} );
                }

            } else {
                // go to sub_activity2 widget
                for (var i = 0; i < api_sub_activities.length; i++) {
                    var key = Object.keys(api_activities[i])[0];
                    this.sub_activities1.push( {text: key, value: key, sub_matrix: api_activities[i][key]} );
                }
            }
        } else {
            for (var i = 0; i < api_activities.length; i++) {
                var key = Object.keys(api_activities[i])[0];
                this.sub_activities1.push( {text: key, value: key, sub_matrix: api_activities[i][key]} );
            }
        }
	},

    chainedSelectSubActivities2: function(activity_name){
		let vm = this;
        vm.sub_activities2 = [];
        vm.categories = [];
        vm.selected_sub_activity2 = '';
        vm.selected_category = '';
        vm.approval_level = '';

        //var api_activities = this.get_sub_matrix(activity_name, vm.sub_activities1[0]['text'])
        var [api_activities, res] = this.get_sub_matrix(activity_name, vm.sub_activities1)
        if (res == "null" || res == null) {
            vm.approval_level = api_activities;
            return;
        } else if (res == "pass") {
            for (var i = 0; i < api_activities.length; i++) {
                this.categories.push( {text: api_activities[i][0], value: api_activities[i][0], approval: api_activities[i][1]} );
            }
        } else {
            for (var i = 0; i < vm.sub_activities1.length; i++) {
                if (activity_name == vm.sub_activities1[i]['text']) {
                    var api_activities2 = vm.sub_activities1[i]['sub_matrix'];
                    for (var j = 0; j < api_activities2.length; j++) {
                        var key = Object.keys(api_activities2[j])[0];
                        this.sub_activities2.push( {text: key, value: key, sub_matrix: api_activities2[j][key]} );
                    }
                }
            }
        }
	},
    chainedSelectCategories: function(activity_name){
		let vm = this;
        vm.categories = [];
        vm.selected_category = '';
        vm.approval_level = '';

        for (var i = 0; i < vm.sub_activities2.length; i++) {
            if (activity_name == vm.sub_activities2[i]['text']) {
                var api_categories = vm.sub_activities2[i]['sub_matrix'];
                for (var j = 0; j < api_categories.length; j++) {
                    this.categories.push( {text: api_categories[j][0], value: api_categories[j][0], approval: api_categories[j][1]} );
                }
            }
        }
	},

    get_sub_matrix: function(activity_name, sub_activities){
        // this.sub_activities1[0]['text']
        if (activity_name in sub_activities) {
            if (sub_activities[activity_name].length > 0) {
                if ('pass' in sub_activities[activity_name][0]) {
                    return [sub_activities[activity_name], "pass"];

                } else if ('null' in sub_activities[activity_name][0]) {
                    if (sub_activities[activity_name]['sub_matrix'] == null) {
                        var approval_level = sub_activities[activity_name][0]['null'][0][0];
                    } else {
                        var approval_level = sub_activities[activity_name]['sub_matrix'][0]['null'][0];
                    }
                    return [approval_level, "null"];
                    //return [sub_activities[activity_name], "null"];
                }
            }
           
            // not a sub_matrix --> this is the main activity_matrix data (as provided by the REST API)
            return [sub_activities[activity_name], true];
        }
        for (var i = 0; i < sub_activities.length; i++) {
            if (activity_name == sub_activities[i]['text']) {
                var key_sub_matrix = Object.keys(sub_activities[i]['sub_matrix'][0])[0];
                if (key_sub_matrix == "null") {
                    var approval_level = sub_activities[i]['sub_matrix'][0]['null'][0];
                    return [approval_level, null]
                } else if (key_sub_matrix == "pass") {
                    return [sub_activities[i]['sub_matrix'][0]['pass'], "pass"]
                } else {
                    return [sub_activities[i]['sub_matrix'][0], true];
                }
            }
        }
    },
    get_approval_level: function(category_name) {
        let vm = this;
        for (var i = 0; i < vm.categories.length; i++) {
            if (category_name == vm.categories[i]['text']) {
                vm.approval_level = vm.categories[i]['approval'];
            }
        }
        
    }

  },
  mounted: function() {
    let vm = this;
    vm.fetchRegions();
    vm.fetchApplicationTypes();
    vm.fetchActivityMatrix();
    vm.form = document.forms.new_proposal;
  },
  beforeRouteEnter: function(to, from, next) {

    let initialisers = [
        utils.fetchProfile(),
        
        //utils.fetchProposal(to.params.proposal_id)
    ]
    next(vm => {
        vm.loading.push('fetching profile')
        Promise.all(initialisers).then(data => {
            vm.profile = data[0];
            //vm.proposal = data[1];
            vm.loading.splice('fetching profile', 1)
        })
    })
    
  }
}
</script>

<style lang="css">
input[type=text], select{
    width:40%;
    box-sizing:border-box;

    min-height: 34px;
    padding: 0;
    height: auto;
}

.group-box {
	border-style: solid;
	border-width: thin;
	border-color: #FFFFFF;
}
</style>
