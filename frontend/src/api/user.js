import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/login',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/user_info',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    // url: 'http://101.133.169.18:8004/api/logout',
    // url: 'http://127.0.0.1:8004/api/logout',
    url: '/logout',
    method: 'post'
  })
}
