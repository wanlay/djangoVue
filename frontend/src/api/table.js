import request from '@/utils/request'

export function fetchList(query) {
  return request({
    url: '/table',
    method: 'get',
    params: query
  })
}

export function updateList(data, pk) {
  return request({
    url: '/table/' + pk,
    method: 'put',
    data: data
  })
}

export function createList(data) {
  return request({
    url: '/table',
    method: 'post',
    data: data
  })
}

export function deleteList(pk) {
  return request({
    url: '/table/' + pk,
    method: 'delete'
  })
}
