import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
Vue.config.devtools = true

export default new Vuex.Store({
  state: {
    baseUrl: 'http://localhost:5000',
    accessToken: '',
  },
  mutations: {
    setToken(state, accessToken) {
      state.accessToken = accessToken
    },
  },
  actions: {},
  modules: {},
})
