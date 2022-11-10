import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    counter:0
  },
  mutations: {
    CNT_CHANGE(state,d){
      state.counter+=d;
    }
  },
  actions: {
    change_cnt(context,d){
      context.commit('CNT_CHANGE',d)
    }
  },
  modules: {
  }
})
