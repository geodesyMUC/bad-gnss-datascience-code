% read in the data
opts = detectImportOptions('sample_data.csv');
data = readtable('sample_data.csv', opts);

% time variables
st = '2023-01-01 00:00:00';
et = '2023-01-01 03:00:00';

% filter data based on timestamp
df_st = data(data.timestamp >= datetime(st) & data.timestamp <= datetime(et), :);

% fill missing values with 0
df_st.num_satellites(isnan(df_st.num_satellites)) = 0;

% extract num_satellites
numSv = df_st.num_satellites;

% plot data number of satellites
figure('Position', [100, 100, 1200, 600]);
hold on;
for i = 1:numel(numSv)
    if numSv(i) < 10
        plot(df_st.timestamp(i), numSv(i), 'r.');
    elseif numSv(i) < 20
        plot(df_st.timestamp(i), numSv(i), 'b.');
    elseif numSv(i) > 20
        plot(df_st.timestamp(i), numSv(i), 'g.');
    end
end
hold off;
xlabel('Time');
ylabel('Number of Satellites');
title('Number of Satellites Over Time');
saveas(gcf, 'satellites_plot_m.png');

% time variables for pdop
st_pdop = '2023-01-01 00:00:00';
et_pdop = '2023-01-01 03:00:00';

% filter data based on timestamp for pdop
df_st_pdop = data(data.timestamp >= datetime(st_pdop) & data.timestamp <= datetime(et_pdop), :);

% fill missing values with 0 for pdop
df_st_pdop.pdop(isnan(df_st_pdop.pdop)) = 0;

% extract pdop values
pdopValues = df_st_pdop.pdop;

% plot pdop over time
figure('Position', [100, 100, 1200, 600]);
plot(df_st_pdop.timestamp, pdopValues);
xlabel('Time');
ylabel('PDOP');
title('PDOP Over Time');
saveas(gcf, 'pdop_plot_m.png');
