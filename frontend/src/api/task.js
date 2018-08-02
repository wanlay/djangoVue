import request from '@/utils/request'

export function fetchList(query, id) {
  return request({
    url: '/api/' + id + '/',
    method: 'get',
    params: query
  })
}

export function updateList(data, id, pk) {
  return request({
    url: '/api/' + id + '/' + pk,
    method: 'put',
    data: data
  })
}

export function createList(data, id) {
  return request({
    url: '/api/' + id + '/',
    method: 'post',
    data: data
  })
}

export function deleteList(id, pk) {
  return request({
    url: '/api/' + id + '/' + pk,
    method: 'delete'
  })
}
