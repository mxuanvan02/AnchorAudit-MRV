# Dữ liệu khí tượng ERA5 dùng trong bài

Sáu file `{can_tho,soc_trang,ca_mau}_{2024,2025}.csv` là chuỗi giờ ERA5 cho ba trạm,
tải qua Open-Meteo Historical Weather API (`https://archive-api.open-meteo.com/v1/archive`)
bằng `data/fetch_era5_multi.py`. Mỗi file có `*.provenance.json` đi kèm ghi thời điểm tải.

Commit sẵn để người đọc chạy lại **đúng** dữ liệu đã sinh các con số trong bài; tải lại
có thể ra số khác nếu nhà cung cấp hiệu chỉnh dữ liệu.

Giấy phép: dữ liệu Open-Meteo phát hành theo CC BY 4.0; ERA5 do Copernicus Climate
Change Service (C3S) / ECMWF cung cấp. Ghi nguồn: Hersbach et al. (2020), ERA5 hourly
data, C3S Climate Data Store; Open-Meteo.com.
