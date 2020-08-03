import Vue from 'vue'
import axios from 'axios'
Vue.prototype.$http = axios
// import defaultSettings from '@/settings'

const root = 'http://localhost:8000/api/'

Vue.prototype.getHttpData = function(url, params, callback) {
  axios.get(root + url, {
    params: params
  }).then((res) => {
    callback(res)
  }).then((res) => {
    console.log(res)
  }).catch((reject) => {

  })
}

Vue.prototype.postHttpData = function(url, params, callback) {
  axios.post(root + url, params).then((res) => {
    callback(res)
  }).then((res) => {
    console.log(res)
  }).catch((reject) => {

  })
}

Vue.prototype.putHttpData = function(url, params, callback) {
  axios.put(root + url, params).then((res) => {
    callback(res)
  }).then((res) => {
    console.log(res)
  }).catch((reject) => {

  })
}
Vue.prototype.patchHttpData = function(url, params, callback) {
  axios.patch(root + url, params).then((res) => {
    callback(res)
  }).then((res) => {
    console.log(res)
  }).catch((reject) => {
  })
}

Vue.prototype.deleteHttpData = function(url, params, callback) {
  axios.delete(root + url, params).then((res) => {
    callback(res)
  }).then((res) => {
    console.log(res)
  }).catch((reject) => {

  })
}
