import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/api/fourgfull',
    method: 'get',
    params: query
  })
}

export function updateList(data, pk) {
  return request({
    url: '/api/fourgfull/' + pk,
    method: 'put',
    data: data
  })
}

export function createList(data) {
  return request({
    url: '/api/fourgfull',
    method: 'post',
    data: data
  })
}

export function deleteList(pk) {
  return request({
    url: '/api/fourgfull/' + pk,
    method: 'delete'
  })
}
