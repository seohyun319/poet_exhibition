export async function fetchGET(url, params = {}) {
	const requestUrl = `${url}?${new URLSearchParams(params)}`

	try {
		const response = await fetch(requestUrl, {
			method: 'GET',
		})
		if (response.status !== 200) {
			throw response
		}
		const data = await response.json()
		return {
			status: response.status,
			data,
		}
	} catch (e) {
		console.error(e)
		return {
			status: e.status ? e.status : null,
			data: null,
		}
	}
}

export async function fetchPOST(url, params = {}) {
	try {
		const response = await fetch(url, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'X-CSRFToken': window.csrfToken,
			},
			body: JSON.stringify(params),
		})
		if (response.status !== 200) {
			throw response
		}
		const data = await response.json()
		return {
			status: response.status,
			data,
		}
	} catch (e) {
		console.error(e)
		return {
			status: e.status ? e.status : null,
			data: null,
		}
	}
}
