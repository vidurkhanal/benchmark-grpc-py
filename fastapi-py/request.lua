-- script.lua
local file_path = "sample_file"

local function read_file_content(path)
    local file = io.open(path, "r")
    if not file then
        return nil
    end
    local content = file:read("*a")
    file:close()
    return content
end

request = function()
    -- Create a multipart/form-data request
    local file_content = read_file_content(file_path)
    if not file_content then
        return nil
    end

    local body = "-----------------------------boundary\r\n"
    body = body .. "Content-Disposition: form-data; name=\"file\"; filename=\"example.txt\"\r\n"
    body = body .. "Content-Type: text/plain\r\n\r\n"
    body = body .. file_content .. "\r\n"
    body = body .. "-----------------------------boundary--\r\n"

    return wrk.format("POST", "/upload-file", {
        ["Content-Type"] = "multipart/form-data; boundary=---------------------------boundary"
    }, body)
end
