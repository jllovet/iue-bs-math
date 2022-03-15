FROM blang/latex:ctanfull

# RUN cp -R /usr/local/texlive/2017/texmf-dist/fonts/* /usr/share/fonts/
RUN ln -s /usr/local/texlive/2017/texmf-dist/fonts/afm /usr/share/fonts/afm && \
ln -s /usr/local/texlive/2017/texmf-dist/fonts/cid /usr/share/fonts/cid && \
ln -s /usr/local/texlive/2017/texmf-dist/fonts/cmap /usr/share/fonts/cmap && \
ln -s /usr/local/texlive/2017/texmf-dist/fonts/enc /usr/share/fonts/enc && \
ln -s /usr/local/texlive/2017/texmf-dist/fonts/lig /usr/share/fonts/lig && \
ln -s /usr/local/texlive/2017/texmf-dist/fonts/map /usr/share/fonts/map && \
ln -s /usr/local/texlive/2017/texmf-dist/fonts/misc /usr/share/fonts/misc && \
ln -s /usr/local/texlive/2017/texmf-dist/fonts/ofm /usr/share/fonts/ofm && \
ln -s /usr/local/texlive/2017/texmf-dist/fonts/opentype /usr/share/fonts/opentype && \
ln -s /usr/local/texlive/2017/texmf-dist/fonts/ovf /usr/share/fonts/ovf && \
ln -s /usr/local/texlive/2017/texmf-dist/fonts/ovp /usr/share/fonts/ovp && \
ln -s /usr/local/texlive/2017/texmf-dist/fonts/pk /usr/share/fonts/pk && \
ln -s /usr/local/texlive/2017/texmf-dist/fonts/sfd /usr/share/fonts/sfd && \
ln -s /usr/local/texlive/2017/texmf-dist/fonts/source /usr/share/fonts/source && \
ln -s /usr/local/texlive/2017/texmf-dist/fonts/tfm /usr/share/fonts/tfm && \
ln -s /usr/local/texlive/2017/texmf-dist/fonts/truetype /usr/share/fonts/truetype && \
ln -s /usr/local/texlive/2017/texmf-dist/fonts/type1 /usr/share/fonts/type1 && \
ln -s /usr/local/texlive/2017/texmf-dist/fonts/vf /usr/share/fonts/vf

RUN apt-get update && \
    apt-get install fontconfig

RUN fc-cache