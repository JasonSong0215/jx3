import request from '@/utils/request'

export function cal(data) {
  return request({
    url: '/api/cal',
    method: 'post',
    data
  })
}
export function authdps(data){
  return request({
    url: '/api/authdps',
    method: 'post',
    data
  })
}
export function test_dps(data){
  return request({
    url: '/api/test_dps',
    method: 'post',
    data
  })
}
export function pwd(data){
  return request({
    url: '/api/pwd',
    method: 'post',
    data
  })
}

